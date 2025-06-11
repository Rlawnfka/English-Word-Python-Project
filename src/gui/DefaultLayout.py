import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from defalut_setting.colors import *

# XXX : stackedLayout 연결이 안됌. 특히 nav와의 연결이 불완전
# nav를 DefaultLayout의 함수로 바꾸면서 해결중
class DefaultLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.HEIGHT = 900
        self.WIDTH = 550
        
        # 기본 세팅, 움직임
        # 전에 열렸던 자리 기억
        self.setStyleSheet(f"""
            *{{
                background-color: {BACKGROUND['main']};
            }}
        """)
        
        self.setWindowTitle("Shorty!")
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 상단에 Logo 고정
        self.layout.addWidget(CreateLogo())

        # 중간 내용 <- 각 페이지의 클래스에서 설정 (상속 통해서)
        self.contentLayout = QVBoxLayout()
        self.stack = QStackedLayout()

        self.contentLayout.addLayout(self.stack)
        
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

        iconHome = QIcon("../assets/icons/iconHome.svg")
        iconAdd = QIcon("../assets/icons/iconAdd.svg")
        iconSetting = QIcon("../assets/icons/iconSetting.svg")
        iconProfile = QIcon("../assets/icons/iconProfile.svg")
        
        iconList = [iconHome, iconAdd, iconSetting, iconProfile]
        page = [0, 3, 1, 2]

        layout = QHBoxLayout()

        for i, icon in enumerate(iconList):
            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(QSize(35,35))
            button.setFlat(True) # 입체감 없애기
            button.setCheckable(True) # 클릭 상태 유지  isChecked()로 확인 후 hover먹이기
            button.clicked.connect(lambda _, index=i: self.stack.setCurrentIndex(page[i])) # 인덱스 끝으로 인식되는 문제 -> index=i로 해결
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
    
        