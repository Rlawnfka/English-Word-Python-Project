from defalut_setting.colors import *
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
        iconHome = QIcon("/assets/icons/iconHome.svg")
        iconAdd = QIcon("/assets/icons/iconAdd.svg")
        iconSetting = QIcon("/assets/icons/iconSetting.svg")
        iconProfile = QIcon("/assets/icons/iconProfile.svg")
        
        iconList = [iconHome, iconAdd, iconSetting, iconProfile]

        layout = QHBoxLayout()

        for i, icon in enumerate(iconList):
            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(QSize(35,35))
            button.setFlat(True) # 입체감
            button.setCheckable(True) # 클릭 상태 유지  isChecked()로 확인 후 hover먹이기
            button.setStyleSheet("""
                                QPushButton{
                                 color: TEXT['primary']
                                 background-color : transparent;
                                }
                                QPushButton::hover{
                                    color: COLOR['hover']
                                }
            """)
            layout.addWidget(button)

        


# 모든 페이지에 나오는 logo, nav 레이아웃 & 
# 페이지 기본 레이아웃 설정~``
class defalutLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.HEIGHT = 900
        self.WIDTH = 550
        self.initUI()

    def initUI(self):
        # 기본 세팅, 움직임
        self.setStyleSheet("""
                           background-color: BACKGROUND['main'];
                           
                           """)
        # 전에 열렸던 자리 기억
        
        self.setWindowTitle("Shorty!")
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 상단에 LOGO 고정하긔..
        self.layout.addWidget(CreateLogo())

        # 중간 
        self.contentLayout = QVBoxLayout()
        self.layout.addLayout(self.contentLayout)

        # 하단 nav 고정
        self.layout.addWidget(CreateNav())




