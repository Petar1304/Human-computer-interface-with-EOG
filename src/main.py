import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import random

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    GREY = 'grey'
    RED = 'red'

    for i in range(0, 3):
        for j in range(0, 3):
            # tile = QPushButton('')
            tile = QLabel(' ')
            if (i == 0 and j == 1):
                tile.setStyleSheet('background-color: red')
            else:
                tile.setStyleSheet(f'background-color: grey') # random.choice(colors)}
            grid.addWidget(tile, i, j)

            
    win.setLayout(grid)
    win.setWindowTitle("EOG Calibration")
    win.setGeometry(200, 200, 1280, 720)
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import random

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    GREY = 'grey'
    RED = 'red'

    for i in range(0, 3):
        for j in range(0, 3):
            # tile = QPushButton('')
            tile = QLabel(' ')
            if (i == 0 and j == 1):
                tile.setStyleSheet('background-color: red')
            else:
                tile.setStyleSheet(f'background-color: grey') # random.choice(colors)}
            grid.addWidget(tile, i, j)

            
    win.setLayout(grid)
    win.setWindowTitle("EOG Calibration")
    win.setGeometry(200, 200, 1280, 720)
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
