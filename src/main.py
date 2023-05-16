from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSlot, QObject, Qt, QThread
import sys
import serial
import random
from grid import Grid
from acquisition import AcquisitionWorker


class MyWindow(QMainWindow):
    # global variable
    active_cell = [1, 2]
    ch1 = ch2 = 0

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowTitle('EOG Calibration')
        self.setupUI()

    def setupUI(self):
        # self.grid = QGridLayout(self)    
        # for i in range(0, 3):
        #     for j in range(0, 3):
        #         self.tile = QLabel(' ', self)
        #         if (i == self.active_cell[0] and j == self.active_cell[1]):
        #             self.tile.setStyleSheet('background-color: red')
        #         else:
        #             self.tile.setStyleSheet(f'background-color: grey') # random.choice(colors)}
        #         self.grid.addWidget(self.tile, i, j)

        # self.create_grid()

        # self.layout = QVBoxLayout()
        # self.layout.addWidget(Grid(self.active_cell))

        self.grid = Grid(self.active_cell)

        self.button = QPushButton('next', self)
        self.button.setStyleSheet('background-color: orange; color: green')
        self.button.clicked.connect(self.change_cell)
        # self.grid.addWidget(self.button, 3, 1, 1, 1)

        # self.layout.addWidget(self.button)
        # self.widget = QWidget()
        self.setCentralWidget(self.grid)
        # self.setLayout(self.grid)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def change_cell(self):
        self.active_cell[0] = random.choice([0, 1, 2])
        self.active_cell[1] = random.choice([0, 1, 2])
        print(self.active_cell)

    def getData(self, ch1, ch2):
        self.ch1, self.ch2 = ch1, ch2
        print(f'>> ch1: {self.ch1} ch2: {self.ch2}')

    def start_acquisition(self):
        self.thread = QThread()
        self.worker = AcquisitionWorker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        # connecting to slot
        self.worker.data.connect(self.getData)


        self.thread.start()


def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    # should be called from ui
    win.start_acquisition()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()




