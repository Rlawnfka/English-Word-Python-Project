import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from gui.page01 import page01

import warnings
warnings.simplefilter("always")

# gui entrance
# create window & event roop

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shorty!")
        self.setFixedSize(550, 900)
        
        self.setCentralWidget(page01())

if __name__ == "__main__":
    # 진입
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# 여기서 위젯 관리 