from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowTitle('EOG Calibration')
        self.setupUI()

    def setupUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.label.move(100, 100)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText('Click me')
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.label.setText('you pressed the button')
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()