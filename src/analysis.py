import numpy as np
import neurokit2

def analyze(data):
    ch1, ch2 = data
    # load thresholds
    th_right, th_left, th_up, th_down = readThresholds()

    command = 'NONE'
    ch1_com = 'NONE'
    ch2_com = 'NONE'
    
   # channel 1
    if ch1 >= th_up:
        ch1_com = 'UP'
    elif ch1 <= th_down:
        ch1_com = 'DOWN'
    # channel 2
    if ch2 >= th_right:
        ch2_com = 'RIGHT'
    elif ch2 <= th_left:
        ch2_com = 'LEFT'
 
    command = [ch1_com, ch2_com]
    return command

def readThresholds():
    inputFile = 'data/thresholds.txt'
    with open(inputFile, 'r') as f:
        data = f.read()
        return [float(val) for val in data.split(',')]


'''
(ch1, ch2)  |   command
-------------------------
(0, 0)          none
ch1 > th1
ch1 < th1
ch2 > th2
ch2 < th2

'''
