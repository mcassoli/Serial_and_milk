# sanitize: RX bike rack serial data cooked and pushed to Rack objects
#   per ME396P-F2022-G03/Standards/board-data-flow.jpeg
#   per "<'Available '> + <distance> <'\n'>" in Bike Arduino/ESP_BT_Handler.py
#   per Bike Arduino/BT_with_info_string_ESP32/BT_with_info_string_ESP32.ino
#   per "Eg_dict = {0 : True, 1: False, 2 : True, 3 : True, 4 : False}" in Standards/Rack_Dict_convention
#   per Bike Arduino/mod_example_sonar_arduino_uno_version/mod_example_sonar_arduino_uno_version.ino

from ESP_BT_Handler import *
from Rack import *
#import Rack as Rack
import re

line_re = None
classifier_data = None
rack = None

def load_classifier_data():
    classifier_data = {'CUTOFF_ONE: 30,'CUTOFF_TWO': 10}

def rack_init(rack_map_data):
    rack = Rack()
    

def sanitize(rack_map_data, port_baud_list=None):
    def parse_line(line):
        return line_re.match(line)
    
    def grammar_is_good(line_data):
        return bool(line_data)
   
    def classify(line_data):
        return {0 : line_data.match(1) == 'AVAILABLE'}
    
    def push_to_rack(the_dict):
        rack.update(the_dict)
        pass
    
    def port_listnener(port):
        line = get_messages(port = 7)  ##### udpate port if necessary (unlikely)
        line_data = parse_line(line)
        if grammar_is_good(line_data):
            the_dict = classify(line_data)
            push_to_rack(the_dict)
    
    port_listener()

def supervise():
    load_classifier_data()
    distance_pat = '(0|[0-9][1-9]*)'
    line_re = re.compile(r'(AVAILABLE|NOT AVAILABLE) ' + distance_pat + '\n')
    rack_init(rack_map_data)
    while True:
        sanitize()
  
if __name__ == '__main__':
    supervise()
