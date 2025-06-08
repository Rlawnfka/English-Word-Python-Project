import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from gui.page01 import page01
from gui.page02 import page02
from gui.page03 import page03
from gui.page03_01 import page03_01
from gui.page04 import page04
from gui.page05 import page05
from gui.page06 import page06

import warnings
warnings.simplefilter("always")



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()

           # index 6

        self.stack.setCurrentIndex(1)
        
        self.setCentralWidget(self.stack)

if __name__ == "__main__":
    # 진입
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# 여기서 위젯 관리 