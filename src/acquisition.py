from PyQt5.QtCore import QObject, QThread, pyqtSignal
import sys, time
import serial
import neurokit2

class AcquisitionWorker(QObject):
    # channels from eog (up/down and left/right movement)
    data = pyqtSignal(int, int)
    
    def __init__(self):
        super().__init__()
        # port for arduino
        self.port = '/dev/ttyUSB0'

    def open_serial(self):
        com_port = self.port
        baud_rate = 9600
        ser = serial.Serial(com_port, baud_rate)
        return ser

    def process_data(self, data):
        data_list = data.strip().split(',')
        data = []
        data[0] = int(data_list[0]) * 5 / 1023
        data[1] = int(data_list[1]) * 5 / 1023
        return data

    def run(self):
        ser = self.open_serial()
        while(True):
            arduino_data = ser.readline()
            print(arduino_data.decode(encoding='ascii', errors='ignore'))
            data = self.process_data(arduino_data)
            # emmiting signal
            self.data.emit(data)
        
        '''
        # testing
        i = 0
        j = 1
        while True:
            time.sleep(1)
            self.data.emit(i, j)
            i += 1
            j += 1
        '''

    def recordChannelData():
        data = []


    def analyze(data):
        ch1, ch2 = data
        # load thresholds
        th1_right, th1_left, th2_up, th2_down = readThresholds()

        command = 'NONE'
        ch1_com = 'NONE'
        ch2_com = 'NONE'
        # analyze signal
        # channel 1
        if ch1 >= th1_right:
            ch1_com = 'RIGHT'
        elif ch1 <= th1_left:
            ch1_com = 'LEFT'
        # channel 2
        if ch2 >= th2_up:
            ch2_com = 'UP'
        elif ch2 <= th2_down:
            ch2_com = 'DOWN'

        command = [ch1_com, ch2_com]
        return command

    def readThresholds():
        inputFile = 'data/thresholds.txt'
        with open(inputFile, 'r') as f:
            data = f.read()
            return [float(val) for val in data.split(',')]

    def saveThresholds(th1_right, th1_left, th2_up, th2_down):
        outputFile = 'data/thresholds.txt'
        with open(outputFile, 'w') as f:
            f.write(f'{th1_right},{th1_left},{th2_up},{th2_down}')

    def clean_eog(eog_signal):
        eog_cleaned = neurokit2.eog_clean(eog_signal, sampling_rate=100, method='neurokit')
        return eog_cleaned


'''
(ch1, ch2)  |   command
-------------------------
(0, 0)          none
ch1 > th1
ch1 < th1
ch2 > th2
ch2 < th2

'''
