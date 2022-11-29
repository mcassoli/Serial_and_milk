import flask
import time

from Rack import rack

app = flask.Flask(__name__)

rack1 = rack()
rack2 = rack()

# print ("Time last updated:",rack1.updated)
# print ("Current status of rack:",rack1.bays)

rack1.UpdateRack({0:True, 1:True, 2:True})

# print (rack2.bays)
# print ("Time last updated:",rack1.updated)
# print ("Current status of rack:",rack1.bays)

# rack1.UpdateRack({0:True, 1:True, 2:True})

# print ("Time last updated:",rack1.updated)
# print ("Current status of rack:",rack1.bays)


bayLocation = []
status = []
for bays in rack1.bays.items():
    
    bayLocation.append(bays[0] + 1)
    # print (bayLocation)
    
    if bays[1] == True:
        status.append("Bay is Full")
    if bays[1] == False:
        status.append("Bay is Empty")
        

# status = rack1.bays.values()
# bays = rack1.bays.keys()

print(status)
print(bayLocation)



@app.route('/')
def home():
    
    
    # data = ""
    
    # for bay in rack1.items():
    #     print (bay)
    #     # data += "<td>" + bay
    
    return flask.render_template("rack1.html", headings = bayLocation, data = status )

# @app.route('/process',methods=["POST"])
# def process():
# 	if flask.request.method == 'POST':
# 		
#         return render_template("rack1.html")


app.run(use_reloader = False, debug = True)
