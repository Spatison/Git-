from PyQt5.QtWidgets import QMainWindow, QPushButton


class ui_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Рисовать', self)
        self.btn.setGeometry(10, 880, 981, 61)
        self.setGeometry(200, 200, 1000, 1000)
