import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from defalut_setting.colors import *

<<<<<<< HEAD
from gui.page01 import page01
from gui.page02 import page02
from gui.page03 import page03
from gui.page03_01 import page03_01
from gui.page04 import page04
from gui.page05 import page05
from gui.page06 import page06


=======
>>>>>>> 9bf9dd1f3bb3c9cc08167dc31002b25b10131d05
class DefaultLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.HEIGHT = 900
        self.WIDTH = 550
        
        # 기본 세팅, 움직임
        self.setStyleSheet(f"""
            *{{
                background-color: {BACKGROUND['main']};
            }}
        """)
        # 전에 열렸던 자리 기억
        
        self.setWindowTitle("Shorty!")
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 상단에 Logo 고정
        self.layout.addWidget(CreateLogo())

        # 중간 내용 <- 각 페이지의 클래스에서 설정 (상속 통해서)
        self.contentLayout = QVBoxLayout()
        self.layout.addLayout(self.contentLayout)

        # 하단 nav 고정
        self.layout.addWidget(CreateNav(self.stack))
        

class CreateLogo(QWidget):
    def __init__(self):
        super().__init__()
        logo = QLabel("Shorty!", self)
        logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        font = QFont("Tilt Warp",32,QFont.Weight.Normal)
        logo.setFont(font)

        logo.setStyleSheet("""
            color: #000000;
            font-size : 32px;
            font-weight: 400;
            font-style: normal;
          """)
        

class CreateNav(QWidget):
    def __init__(self, stack: QStackedLayout):      # 스택을 받아서 사용 DefaultLayout -> CreateNav
        super().__init__()
        self.stack = stack

        self.stack = QStackedLayout()   # 인덱스 동작 -> 처음 선언 순으로 0 씩 증가 
        self.stack.addWidget(page01())  # 
        self.stack.addWidget(page02())
        self.stack.addWidget(page03())
        self.stack.addWidget(page03_01())
        self.stack.addWidget(page04())
        self.stack.addWidget(page05())
        self.stack.addWidget(page06())

        iconHome = QIcon("../assets/icons/iconHome.svg")
        iconAdd = QIcon("../assets/icons/iconAdd.svg")
        iconSetting = QIcon("../assets/icons/iconSetting.svg")
        iconProfile = QIcon("../assets/icons/iconProfile.svg")
        
        iconList = [iconHome, iconAdd, iconSetting, iconProfile]

        layout = QHBoxLayout()

        for i, icon in enumerate(iconList):
            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(QSize(35,35))
            button.setFlat(True) # 입체감 없애기
            button.setCheckable(True) # 클릭 상태 유지  isChecked()로 확인 후 hover먹이기
            button.clicked.connect(lambda: self.stack.setCurrentIndex(i))
            button.setStyleSheet(f"""
                QPushButton{{
                    color: {TEXT['primary']};
                    background-color : transparent;
                }}
                QPushButton:hover{{
                    color: {COLOR['hover']};
                }}
            """)
            layout.addWidget(button)
    
    
        