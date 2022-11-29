# RFC: sanitizer's inputs from RX (cf board-data-flow.jpeg)

# example: result of last two "print"s of this file

# sanitizer to determine full or empty based on rack data received by doing classification against calibration data

# code of ESP32S_NdeMCU_Bluetooth_Broadcast_initial.ino which fall in sanitizer scope
#   line 37:distance = duration * 0.034 / 2
#   lines 42...:if(distance < DIST_THRESH){...

import numpy as np
import collections  # cf. page 15 of meet/1004/13 CS numpy and matplotlib.pptx.pdf

rack_name = 'etc_front'

# number of samples per chunk
nsamp = 7

# sensor characteristics
OpPt = collections.namedtuple('OpPt', ('μ','σ') )  # operating point
Snsr = collections.namedtuple('Snsr', ('empty','full') )  # sensor

nsnsr = 3
σ = .05  # assume same for all sensors and distances for this example of data format

snsr_calib = [Snsr(empty=OpPt(μ + 50,σ),full=OpPt(μ,σ)) for μ in random.choices(range(10,10+10),k=nsnsr)]
snsr_phys_min,snsr_phys_max = (lambda μs:(max(0,min(μs) - 3 * σ),max(μs) + 3 * σ))([μ for snsr in snsr_calib for μ,_ in snsr])

calib_data = (nsnsr,sum(sum(list(map(lambda x:list(map(list,x)),snsr_calib)),[]),[]))

# sensor physical state
snsr_state = random.choices([False,True],k=nsnsr)  # per board-data-flow.jpeg: True = "Full", False = "Empty
snsr_phys = np.array([[(lambda oppt:random.normalvariate(oppt.μ,oppt.σ))(snsr_calib[snsr_idx][snsr_state[snsr_idx]]) for snsr_idx in range(nsnsr)] for _ in range(nsamp)])

# pulse characteristics: captures typical values of what pulseIn returns
pulse_bits = 16
pulse_top = 2**pulse_bits
pulse_min,pulse_max = 0,pulse_top - 1

# simulate pulseIn for a given physical state
def pulse_sim(phys):
    return int(np.floor(min(pulse_max,max(pulse_min,pulse_top * (phys - snsr_phys_min) / (snsr_phys_max - snsr_phys_min)))))

# sensor samples
snsr_pulse = np.array([pulse_sim(phys) for phys in snsr_phys.reshape(nsnsr * nsamp)]).reshape(snsr_phys.shape)

rack_data = (nsnsr,nsamp,list(snsr_pulse.T.reshape(nsnsr * nsamp)))

# would like sanitizer to read two types of string:

# calibration data
print(f"C:{calib_data}")

# rack data
print(f"R:{rack_data}")
