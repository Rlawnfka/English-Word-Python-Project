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

from gui.page01 import page01
from gui.page02 import page02
from gui.page03 import page03
from gui.page03_01 import page03_01
from gui.page04 import page04
from gui.page05 import page05

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.DefLayout = DefaultLayout()
        self.setCentralWidget(self.DefLayout)

        # 페이지 추가
        self.DefLayout.addPage(page01(self.DefLayout.stack))#home
        self.DefLayout.addPage(page04())#단어추가 페이지
        self.DefLayout.addPage(page05())#setting
        self.DefLayout.addPage(page02())#list(profile)
        self.DefLayout.addPage(page03())#단어 상세페이지
        self.DefLayout.addPage(page03_01())

        # 하단 네비게이션 연결
        self.DefLayout.setNav(CreateNav(self.DefLayout.stack))

        self.setStyleSheet(f"""
            background-color: {BACKGROUND['main']};
        """)
          
    def center(self): # 화면 정가운데로 보내기
        screen = QCoreApplication.instance().primaryScreen()
        rect = screen.availableGeometry()
        center_point = rect.center()
        frame_geom = self.frameGeometry()
        frame_geom.moveCenter(center_point)
        self.move(frame_geom.topLeft())


    # def CreateNav(self, stack):
    #     nav = QWidget()
    #     layout = QHBoxLayout()
        
    #     iconHome = QIcon("../assets/icons/iconHome.svg")
    #     iconAdd = QIcon("../assets/icons/iconAdd.svg")
    #     iconSetting = QIcon("../assets/icons/iconSetting.svg")
    #     iconProfile = QIcon("../assets/icons/iconProfile.svg")
        
    #     iconList = [iconHome, iconAdd, iconSetting, iconProfile]
    #     pages = [0, 3, 1, 2]
    #     for i, icon in enumerate(iconList):
    #         btn = QPushButton()
    #         btn.setIcon(icon)
    #         btn.setIconSize(QSize(35, 35))
    #         btn.setFlat(True)
    #         btn.setCheckable(True)
    #         btn.setStyleSheet(f"""
    #             QPushButton{{
    #                 color: {TEXT['primary']};
    #                 background-color : transparent;
    #             }}
    #             QPushButton:hover{{
    #                 color: {COLOR['hover']};
    #             }}
    #         """)

    #         btn.clicked.connect(lambda _, i=i: stack.setCurrentIndex(i))
    #         layout.addWidget(btn)

    #     nav.setLayout(layout)
    #     return nav



if __name__ == "__main__":
    # 진입
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.center()
    sys.exit(app.exec())

# 여기서 위젯 관리 