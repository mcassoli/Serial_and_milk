# -*- coding: utf-8 -*-
"""
@author: casso

Bluetooth ESP handling and testing module - updated 11/27/22

worekd Nov 15 with COM18
worked Nov 27 with COM4 - it depends on your computer
"""

import serial.tools.list_ports
import time
import random

MESSAGES_PER_QUERY = 10
TIMEOUT = 5

FAKE_DATA = {}
FAKE_DATA[1] = ['AVAILABLE 20\n', 'AVAILABLE 20\n', 'AVAILABLE 20\n', 'AVAILABLE 20\n', 'AVAILABLE 20\n', 'AVAILABLE 20\n', 'AVAILABLE 20\n', 'AVAILABLE 20\n', 'AVAILABLE 20\n', 'AVAILABLE 20\n']
FAKE_DATA[2] = ['AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n']
FAKE_DATA[3] = ['NOT AVAILABLE 13\n', 'NOT AVAILABLE 6\n', 'NOT AVAILABLE 5\n', 'NOT AVAILABLE 4\n', 'NOT AVAILABLE 5\n', 'NOT AVAILABLE 5\n', 'NOT AVAILABLE 3\n', 'NOT AVAILABLE 3\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n', 'AVAILABLE 15\n']
FAKE_DATA[4] = ['NOT AVAILABLE 1\n', 'NOT AVAILABLE 1\n', 'NOT AVAILABLE 1\n', 'NOT AVAILABLE 1\n', 'NOT AVAILABLE 1\n', 'NOT AVAILABLE 1\n', 'NOT AVAILABLE 1\n', 'NOT AVAILABLE 1\n', 'NOT AVAILABLE 1\n', 'NOT AVAILABLE 1\n']


def port_info():
    '''
    prints information about the active / available COM ports
    NOTE these are all the ports your computer has access to. Some may be in
    use by other applications. The COM port must not be in use by other
    applications for Python to access it. Restarting the console and closing
    other applications may help fix this problem.
    '''
    
    ports = serial.tools.list_ports.comports()
    
    portsList = []
    
    for onePort in ports:
        portsList.append(str(onePort))
        print(str(onePort))
        
    pass

def get_messages(port = 4, fake = -1, message_len = 10):
    '''
    Returns a list of strings which are messages from the ESP. Strings within
    the list take the following format:
        <'Available '> + <distance> <'\n'>
        Where the first element could be 'Available' or 'Not Available' and 
        represents the ESP's instantaneous guess as to if the slot is occupied
        The Distance is very approximtely in cm.
        
    If port is specified, that COM port is used. If port is not specified, port
    4 is used. (a typical Bluetooth receiving port)
    
    fake: optional input, int
        -1:   (default) do not send fake data. send real data
         0:    return a randomly created fake string (for when not actually connected to bluetooth)
         1-4:  return a specific fake output (for debugging)
    
    message_len: how many strings you want in the returned list. default 10
    
    If we do not receive messages from the given port, there is a timeout of around .1*message_len seconds.
    
    '''
    
    if fake < 0:
        serialInst = serial.Serial()
        
        val = port
        
        for x in range(0,len(portsList)):
            if portsList[x].startswith("COM" + str(val)):
                portVar = "COM" + str(val)
                print(portVar)
        
        serialInst.baudrate = 9600
        serialInst.port = portVar
        serialInst.open()
        
        messages = []
        
        count = 0
        while len(messages) < message_len and count < TIMEOUT:
            
            if serialInst.in_waiting:
                packet = serialInst.readline()
                messages.append((packet.decode('utf')))
            
            else:        
                time.sleep(.1)
                count += 1
                    
        serialInst.close()
    elif fake == 0:
        choice = random.choice((1, 2, 3, 4))
        messages = FAKE_DATA[choice]
    else:
        messages = FAKE_DATA[fake]
    
    return messages

if __name__ == '__main__':
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    
    portsList = []
    
    for onePort in ports:
        portsList.append(str(onePort))
        print(str(onePort))
    
    val = input("Select Port: COM")
    
    for x in range(0,len(portsList)):
        if portsList[x].startswith("COM" + str(val)):
            portVar = "COM" + str(val)
            print(portVar)
    
    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.open()
    
    messages = []
    print('Listening')
    
    count = 0
    while len(messages) < MESSAGES_PER_QUERY and count < TIMEOUT:
        
        if serialInst.in_waiting:
            packet = serialInst.readline()
            messages.append((packet.decode('utf')))
        
        else:        
            time.sleep(.1)
            count += 1
            
    print(messages)
    
    serialInst.close()