# sanitize: RX bike rack serial data cooked and pushed to Rack objects
#   per ME396P-F2022-G03/Standards/board-data-flow.jpeg
#   per "<'Available '> + <distance> <'\n'>" in Bike Arduino/ESP_BT_Handler.py
#   per DIST_THRESH in Bike Arduino/BT_with_info_string_ESP32/BT_with_info_string_ESP32.ino
#   per "Eg_dict = {0 : True, 1: False, 2 : True, 3 : True, 4 : False}" in Standards/Rack_Dict_convention
#   per Bike Arduino/mod_example_sonar_arduino_uno_version/mod_example_sonar_arduino_uno_version.ino

from ESP_BT_Handler import *
from Rack import *
#import Rack as Rack
import re
from collections import namedtuple

line_re = None
classifier_data = None
rack = None

def load_classifier_data():
    classifier_data = {'DIST_THRESH': 15}

def parse_setup():
    distance_pat = '(0|[0-9][1-9]*)'
    availability_pat = '(AVAILABLE|NOT AVAILABLE)'
    line_re = re.compile(r'' + distance_pat + availability_pat + '\n')
    
def rack_init(rack_map_data):
    rack = Rack()

LineData = namedtuple('LineData', ['availability', 'distance'])

def sanitize():
    def parse_raw_lines(raw_lines):
        rx_matching_lines = []
        for raw_line in raw_lines:
            match = line_re.match(raw_line)
            if match:
                availability = match[1][0] != 'A'
                distance = int(match[0])
                rx_matching_lines.append(LineData(availability=availability,distance=distance))
        return 
    
    def grammar_is_good(line_data):
        return len(line_data)  # using truthiness
   
    def classify(line_data):
        return {0 : line_data[0].availability}  # hack: just return whatever is in the first element (there is one because grammar_is_good)
    
    def push_to_rack(the_dict):
        rack.update(the_dict)
        pass
    
    def port_listnener(port):
        raw_lines = get_messages(port = 7)  ##### udpate port if necessary (unlikely)
        line_data = parse_raw_lines(raw_lines)
        if grammar_is_good(line_data):
            the_dict = classify(line_data)
            push_to_rack(the_dict)
    
    port_listener()

def supervise():
    load_classifier_data()
    parse_setup()
    rack_init(rack_map_data)
    while True:
        sanitize()
  
if __name__ == '__main__':
    supervise()
 
