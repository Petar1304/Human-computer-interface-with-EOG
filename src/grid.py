from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout


class Grid(QWidget):
    def __init__(self, active_cell):
        super().__init__()
        self.active_cell = active_cell
        # self.setGeometry(100, 100, 1280, 720)
        self.setupUI()

    def setupUI(self):
        self.grid = QGridLayout(self)
        for i in range(0, 3):
            for j in range(0, 3):
                self.tile = QLabel(' ', self)
                if (i == self.active_cell[0] and j == self.active_cell[1]):
                    self.tile.setStyleSheet('background-color: red')
                else:
                    self.tile.setStyleSheet(f'background-color: grey') # random.choice(colors)}
                self.grid.addWidget(self.tile, i, j)        

        self.setLayout(self.grid)

    def change_cell(self):
        self.active_cell[0] = random.choice([0, 1, 2])
        self.active_cell[1] = random.choice([0, 1, 2])
        print(self.active_cell)

