# -*- coding: utf-8 -*-
"""
WE HAZ COPYRIGHTS.

Github for observers: https://github.com/mcassoli/Serial_and_milk

Python 3.7
Created on Tue Oct 11 17:53:45 2022

@author: casso

Script to allow Arduino Uno with button attached to send serial messages
to this computer which then sends appropriate serial messages to 
arduino Leonardo which has LED that turns on / off.

Change DELAY_TIME to increase refresh rate.
Change MAX_TIME to increase / decrease iterations

Make sure to use serial.close() to close connections if programs quits
early (or just kill the console)

Other serial connections (eg Arduino ID serial monitor or uploader) will
prevent serial library in python from connecting.

Make sure to update the first arguments of the serial.Serial object creators
with the appropriate COM ports for your computer.

To see what ports you have available:
from serial.tools import list_ports
list_ports.main()

"""

import serial
from time import sleep

UNO_PORT = 'COM3'
LEONARDO_PORT = 'COM11'
DELAY_TIME = .1 #in seconds

on_message = bytes('e', 'utf-8')
off_message = bytes('a', 'utf-8')
MAX_TIME = 200

uno = serial.Serial(UNO_PORT, 9600)
leonardo = serial.Serial(LEONARDO_PORT, 9600)

uno_buffer = []
elapsed = 0

while elapsed < MAX_TIME:
    elapsed += 1
    
    #get rid of all the old lines
    uno.flushInput()
    
    #so that we can read just the latest line
    uno_msg = uno.readline()
    uno_buffer.append(bytes.decode(uno_msg))

    print('\nuno message: ', uno_msg)
    
    if '0' in uno_buffer[-1]:
        print('lights on!')
        leonardo.write(on_message)
    else:
        print('lights off!')
        leonardo.write(off_message)
        
    sleep(DELAY_TIME)
    
print('time elapsed')

uno.close()
leonardo.close()


#individually turn on and off the Leonardo LED:
# leo = serial.Serial('COM13', 9600)
# on_message = bytes('e', 'utf-8')
# off_message = bytes('a', 'utf-8')
# leo.write(on_message)
# leo.write(off_message)
# leo.close()