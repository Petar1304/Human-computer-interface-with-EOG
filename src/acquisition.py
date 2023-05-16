from PyQt5.QtCore import QObject, QThread, pyqtSignal
import sys

class AcquisitionWorker(QObject):
    # channels from eog (up/down and left/right movement)
    ch1 = pyqtSignal()
    ch2 = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        # port for arduino
        self.port = 'dev/tty/ACM0'
        run_thread = True

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
        while(self.run_thread):
            arduino_data = ser.readline().decode()
            self.ch1, self.ch2 = self.process_data(arduino_data)
            self.ch1.emit(self.ch1)
            self.ch2.emit(self.ch2)


