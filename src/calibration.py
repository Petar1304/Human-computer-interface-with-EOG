import numpy as np
import neurokit2
import time
from acquisition import readData

# time for which each direction will be recorded (in seconds)
RECORDING_TIME = 5
SAMPLING_RATE = 100

def record():
    timeout = time.time() + RECORDING_TIME
    data = []
    while time.time() <= timeout:
        data.append(readData())
    return np.array(data)

def readThresholds():
    inputFile = 'data/thresholds.txt'
    with open(inputFile, 'r') as f:
        data = f.read()
        return [float(val) for val in data.split(',')]

def saveThresholds(th1_right, th1_left, th2_up, th2_down):
    outputFile = 'data/thresholds.txt'
    with open(outputFile, 'w') as f:
        f.write(f'{th1_right},{th1_left},{th2_up},{th2_down}')

def clean_eog(data):
    ch1_cleaned = neurokit2.eog_clean(data[:, 0], sampling_rate=SAMPLING_RATE, method='neurokit')
    ch2_cleaned = neurokit2.eog_clean(data[:, 1], sampling_rate=SAMPLING_RATE, method='neurokit')
    return eog_cleaned

def findThreshold(data, direction):
    '''
    data is numpy array
    directions: 'UP', 'DOWN', 'LEFT', 'RIGHT'
    '''
    ch1 = data[:, 0]
    ch2 = data[:, 1]
    
    if direction == 'UP':
        threshold = ch1.mean()
    elif direction == 'DOWN':
        threshold = ch1.mean()
    elif direction == 'RIGHT':
        threshold = ch2.mean()
    elif direction == 'LEFT':
        threshold = ch2.mean()
    return threshold

def calibrate():
    # th1_right, th1_left, th2_up, th2_down = 0.0, 0.0, 0.0, 0.0
    directions = ['UP', 'DOWN', 'RIGHT', 'LEFT']
    thresholds = []
    for direction in directions:
        print(f'>> Look {direction} for {RECORDING_TIME} seconds')
        time.sleep(1)
        print('RECORDING...')
        data = record()
        thresholds.append(findThreshold(data, direction)) 
    if len(thresholds) == 4:
        saveThresholds(*thresholds)
