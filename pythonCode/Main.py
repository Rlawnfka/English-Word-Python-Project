import sys
import os
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self) :    
        self.setWindowTitle("Shorty!")
        self.setGeometry(550,30,450,786)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(300,200,300,300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
