import sys
import colors as color # 색상파일 import
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class CreateLogo(QWidget):
    def __init__(self):
        super().__init__()
        logo = QLabel("Shorty!", self)
        logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        font = QFont("Tilt Warp",32,QFont.Weight.regular)
        logo.setFont(font)

        logo.setStyleSheet("""
            color: #000000;
            font-size : 32px;
            font-family: "Tilt Warp", sans-serif;
            font-optical-sizing: auto;
            font-weight: 400;
            font-style: normal;
            font-variation-settings: "XROT" 0,"YROT" 0;
          """)
        
class CreateNav(QWidget):
    def __init__(self):
        super().__init__()
        iconHome = QIcon("/assets/icons/iconHome.png")
        iconAdd = QIcon("/assets/icons/iconAdd.png")
        iconSetting = QIcon("/assets/icons/iconSetting.png")
        iconProfile = QIcon("/assets/icons/iconProfile.png")


class defalut(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 기본 세팅, 움직임
        self.setStyleSheet(f"background-color:{color.background['main']}") # 배경색 입히기 f-string (문자열 포맷팅)
        self.setWindowTitle('Shorty!') # 타이틀 설정
        self.setGeometry(550,30,450,786) # Gui창 위치, 크기
        # 전에 열렸던 자리 기억
        pass




