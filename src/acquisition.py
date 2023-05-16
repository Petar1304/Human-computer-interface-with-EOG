from PyQt5.QtCore import QObject, QThread, pyqtSignal
import sys, time

class AcquisitionWorker(QObject):
    # channels from eog (up/down and left/right movement)
    data = pyqtSignal(int, int)
    
    def __init__(self):
        super().__init__()
        # port for arduino
        self.port = 'dev/tty/ACM0'

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
        '''
        ser = self.open_serial()
        while(True):
            arduino_data = ser.readline().decode()
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
        





