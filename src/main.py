import sys
from PyQt6.QtWidgets import( 
    QApplication, QMainWindow, QStackedWidget, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton
)
from PyQt6.QtGui import(
    QIcon,
) 
from PyQt6.QtCore import(
    QSize, QCoreApplication
)

import warnings                 # 오류 표시
warnings.simplefilter("always")

from gui.DefaultLayout import DefaultLayout, CreateNav
from defalut_setting.colors import *
from data.word_manager import ConnectDB

from gui.page01 import page01
from gui.page02 import page02
from gui.page03 import page03
from gui.page03_01 import page03_01
from gui.page04 import page04
from gui.page05 import page05

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.connect = ConnectDB()
        self.db = self.connect.db # 여기서 한 번만 연결

        def closeDB(self,event):
            ConnectDB().client.close()
            event.accept()

        self.DefLayout = DefaultLayout()
        self.setCentralWidget(self.DefLayout)
        self.windows = []

        self.HEIGHT = 790
        self.WIDTH = 550
        self.setWindowTitle("Shorty! - main")
        self.setFixedSize(self.WIDTH, self.HEIGHT)

        # main에 위치한 stack --- 여기서 인자로 넘겨줌.
        self.DefLayout.addPage(page01(self.DefLayout.stack))#home
        self.DefLayout.addPage(page04(self.db))#단어추가 페이지
        self.DefLayout.addPage(page05(self, self.db))#setting
        self.DefLayout.addPage(page02(self.db))#list(profile)
        self.DefLayout.addPage(page03())#단어 상세페이지
        self.DefLayout.addPage(page03_01())

        self.DefLayout.setNav(CreateNav(self.DefLayout.stack))

        self.setStyleSheet(f"""
            background-color: {BACKGROUND['main']};
        """)

        self.windows.append(self)
          
    def center(self): # 화면 정가운데로 보내기
        screen = QCoreApplication.instance().primaryScreen()
        rect = screen.availableGeometry()
        center_point = rect.center()
        frame_geom = self.frameGeometry()
        frame_geom.moveCenter(center_point)
        self.move(frame_geom.topLeft())



if __name__ == "__main__":
    # 진입
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.center()
    sys.exit(app.exec())
