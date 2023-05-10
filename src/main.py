import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QObject
import serial
import random

# port for arduino
PORT = 'dev/tty/ACM0'
ACTIVE_CELL = [1, 2]

def change_cell():
    ACTIVE_CELL[0] = random.choice([0, 1, 2])
    ACTIVE_CELL[1] = random.choice([0, 1, 2])
    print(ACTIVE_CELL)

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()    

    for i in range(0, 3):
        for j in range(0, 3):
            tile = QLabel(' ')
            if (i == ACTIVE_CELL[0] and j == ACTIVE_CELL[1]):
                tile.setStyleSheet('background-color: red')
            else:
                tile.setStyleSheet(f'background-color: grey') # random.choice(colors)}
            grid.addWidget(tile, i, j)

    button = QPushButton('next')
    button.setStyleSheet('background-color: orange; color: green')
    button.clicked.connect(change_cell)
    grid.addWidget(button, 3, 1, 1, 1)
    
    win.setLayout(grid)
    win.setWindowTitle("EOG Calibration")
    win.setGeometry(200, 200, 1280, 720)
    win.show()
    sys.exit(app.exec_())


class AcquisitionWorker(QObject):
    # def __init__(self):
        # super().__init__()

    def open_serial(self):
        com_port = PORT
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

if __name__ == '__main__':
    window()
