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

def sanitize(rack_map_data, port_baud_list=None):
    def load_classifier_data():
        pass
    
    def rack_map_init(rack_map_data):
        pass
    
    def parse_line(line):
        # leaning towards lark vs ply based on
        #   https://wiki.python.org/moin/LanguageParsing
        #     "LALR(1) for speed or Earley parser for any context-free grammar."
        #   https://tomassetti.me/parsing-in-python/
        #     "This means that they are clean and readable, but also that you have to traverse the resulting tree yourself"
        #   https://python.libhunt.com/compare-lark-vs-ply
        #     "Compare Lark and PLY's popularity and activity"
        #   https://github.com/lark-parser/lark
        #     "Generate a stand-alone parser (for LALR(1) grammars)"
        #     "Comparison to other libraries"
        #   https://news.ycombinator.com/item?id=28259458
        #     "by far the easiest parser generator I've ever used"
        pass
    
    def grammar_is_good(ast):
        pass
   
    def classify_and_push(ast):
        pass
    
    def port_listnener(port):
        # does not return => lives in own thread
        while True:
            line = port.readline()
            ast = parse_line(line)
            if grammar_is_good(ast):
                classify_and_push(ast)
    
    def ports_init(port_baud_list):
        # maybe serial.tools.list_ports.comports()
        # maybe adjust datarate on each port until see grammar_is_good
        # no writing to ports!
        # timeout for dead ports
        # create port_listnener thread for each port with meaningful data
        # each port_listnener does not return => lives in own thread
        pass
    
    load_classifier_data()
    rack_map_init(rack_map_data)
    ports_init(port_baud_list)
    # return so that other things can happen; e.g., other initialization, flask stuff, ...
    return
  
