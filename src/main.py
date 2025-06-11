import sys
from PyQt6.QtWidgets import( 
    QApplication, QMainWindow, QStackedWidget, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, Qsize
)
from PyQt6.QtGui import(
    QIcon,
) 
from PyQt6.QtCore import(
    QSize
)

import warnings                 # 오류 표시
warnings.simplefilter("always")

from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

from gui.page01 import page01
from gui.page02 import page02
from gui.page03 import page03
from gui.page03_01 import page03_01
from gui.page04 import page04
from gui.page05 import page05

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.setCentralWidget(DefaultLayout())

        self.DefLayout = DefaultLayout()
        self.setCentralWidget(self.DefLayout)

        self.setStyleSheet(f"""
            *{{
                background-color: {BACKGROUND['main']};
            }}
        """)
        
        self.stack = QStackedWidget()
        self.stack.addWidget(page01())  # 홈        0
        self.stack.addWidget(page02())  # 리스트    3
        self.stack.addWidget(page03())  # 리스트 -> 상세
        self.stack.addWidget(page03_01())
        self.stack.addWidget(page04())  # 추가      1
        self.stack.addWidget(page05())  # 세팅      2

        self.layout.setContnet(self.stack)
        self.layout.setNav(self.createNav())
    
    def createNav(self):
        nav = QWidget()
        layout = QHBoxLayout()
        
        iconHome = QIcon("../assets/icons/iconHome.svg")
        iconAdd = QIcon("../assets/icons/iconAdd.svg")
        iconSetting = QIcon("../assets/icons/iconSetting.svg")
        iconProfile = QIcon("../assets/icons/iconProfile.svg")
        
        iconList = [iconHome, iconAdd, iconSetting, iconProfile]
        pages = [0, 3, 1, 2]
        for i, icon in enumerate(iconList):
            btn = QPushButton()
            btn.setIcon(icon)
            btn.setIconSize(QSize(35, 35))
            btn.setFlat(True)
            btn.setCheckable(True)
            btn.setStyleSheet(f"""
                QPushButton{{
                    color: {TEXT['primary']};
                    background-color : transparent;
                }}
                QPushButton:hover{{
                    color: {COLOR['hover']};
                }}
            """)

            btn.clicked.connect(lambda _, i=i: self.stack.setCurrentIndex(i))
            layout.addWidget(btn)

        nav.setLayout(layout)
        return nav



if __name__ == "__main__":
    # 진입
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# 여기서 위젯 관리 