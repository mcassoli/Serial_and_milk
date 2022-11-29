# -*- coding: utf-8 -*-
"""
Python 3.7
Created on Sun Oct 30 01:57:30 2022

@author: casso

https://stackoverflow.com/questions/28800614/run-while-loop-concurrently-with-flask-server
"""

from time import sleep
import serial
from flask import Flask
import threading

CUTOFF_1 = 10

MEGA_PORT = 'COM7'
mega = serial.Serial(MEGA_PORT, 9600)

app = Flask(__name__)

def update_bike_status():
    
    mega.flushInput()
    mega.readline()
    msg = mega.readline()
    
    try: 
        return (eval(msg) > CUTOFF_1, msg)
    except:
        return update_bike_status()

@app.route('/')
def home():
    
    status = update_bike_status()
    
    if status[0]:
        return '<h1> available <br><br></h1>' + str(status[1])
    else:
        return '<h1> NOT available <br><br> </h1>' + str(status[1])
    
    return 'junk'


app.debug = True
app.run(use_reloader=False)
# threads = list()

# a = threading.Thread(target=app.run, args=(debug=True))
# threads.append(a)
# a.start()

# s = threading.Thread(status_checker)
# threads.append(s)
# s.start()