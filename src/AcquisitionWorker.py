from PyQt5.QtCore import QObject

class AcquisitionWorker(QObject):
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
        data_dict = dict()
        data_dict['ch1'] = int(data_dict[0])
        return data_dict

    def run(self):
        ser = self.open_serial()
        arduino_data = ser.readline().decode()
        data = self.process_data(arduino_data)



