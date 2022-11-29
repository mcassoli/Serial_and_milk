# sanitize: RX bike rack serial data cooked and pushed to Rack objects
#   per ME396P-F2022-G03/Standards/board-data-flow.jpeg
# 
# revision
#   2022-11-06: v1, initial
#     not much here, but notes and stubs
#     rack dump format is TBD, but using parser-generator avoids some redevelopment
# 
# overview:
#   * called somehow during initialization of python side of Bike Arduino
#       all rack dump windows reset
#   * if called with port_baud_list=None, then
#       goes through available comports and datarates listening for meaningful data
#   * available comports determined by one of the methods in
#       https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
#   * datarates are the "standard values" listed in
#       https://pyserial.readthedocs.io/en/latest/pyserial_api.html
#   * meaningful data is an entire rack dump (in https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)
#       each rack has some number (>=1) of bays
#       each bay has some number (>=1) of sensors
#       rack dump format is TBD
#   * rack dump data fills a rack dump window (one per rack)
#   * when rack dump window is full
#       new rack dump causes oldest rack dump to leave window
#       rack dump window is classified for each bay
#       classifier results sent to rack object via update_rack

from ESP_BT_Handler import *
from Rack import *
#import Rack as Rack
import re

rack = None

def load_classifier_data():
    pass

def rack_init(rack_map_data):
    rack = Rack()
    

def sanitize(rack_map_data, port_baud_list=None):
    def parse_line(line):
        pass
    
    def grammar_is_good(ast):
        pass
   
    def classify(ast):
        ''' return t/f '''
        #return the_dict
    
    def push_to_rack(the_dict):
        rack.update(the_dict)
        pass
    
    def port_listnener(port):
        get_messages(port = 7)  ##### udpate port if necessary (unlikely)
        ast = parse_line(line)
        if grammar_is_good(ast):
            the_dict = classify(ast)
            push_to_rack(the_dict)
    
    port_listener()

def supervise():
    load_classifier_data()
    rack_init(rack_map_data)
    while True:
        sanitize()
  
if __name__ == '__main__':
    supervise()
