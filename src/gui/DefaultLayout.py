import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from defalut_setting.colors import *


class DefaultLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.HEIGHT = 790
        self.WIDTH = 550

        self.setWindowTitle("Shorty!")
        self.setFixedSize(self.WIDTH, self.HEIGHT)

        self.setStyleSheet(f"""
            *{{
                background-color: {BACKGROUND['main']};
            }}
        """)


        # 전체 레이아웃
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # ----- 상단 로고
        self.logoWidget = CreateLogo()
        self.layout.addWidget(self.logoWidget)

        # ----- 중단 컨텐츠 영역 (Stacked Layout)
        self.stack = QStackedLayout()
        self.contentWidget = QWidget()
        self.contentWidget.setLayout(self.stack)
        self.layout.addWidget(self.contentWidget)

        # ----- 하단 Nav (초기값으로 빈 위젯, 나중에 교체)
        self.navWidget = QWidget()
        self.layout.addWidget(self.navWidget)

    def addPage(self, widget):
        """Stack에 페이지 추가"""
        self.stack.addWidget(widget)

    def setContent(self, index: int):
        """현재 보여줄 페이지 설정"""
        self.stack.setCurrentIndex(index)

    def setNav(self, navWidget):
        """하단 네비게이션을 교체"""
        self.layout.replaceWidget(self.navWidget, navWidget)
        self.navWidget.deleteLater()
        self.navWidget = navWidget
        self.layout.addWidget(self.navWidget)


class CreateLogo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        logo = QLabel("Shorty!", self)
        logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        font = QFont("Tilt Warp", 32, QFont.Weight.Bold)
        logo.setFont(font)

        logo.setStyleSheet("""
            color: #000000;
            font-size: 32px;
            font-weight: 400;
            font-style: normal;
        """)
        layout.addWidget(logo)


class CreateNav(QWidget):
    def __init__(self, stack: QStackedLayout):
        super().__init__()
        self.stack = stack

        # 상대 경로 -> 절대 경로로 변환
        homeIcon_path = os.path.join(os.path.dirname(__file__), "../assets/icons/iconHome.svg")
        addIcon_path = os.path.join(os.path.dirname(__file__), "../assets/icons/iconAdd.svg")
        settingIcon_path = os.path.join(os.path.dirname(__file__), "../assets/icons/iconSetting.svg")
        profileIcon_path = os.path.join(os.path.dirname(__file__), "../assets/icons/iconProfile.svg")

        iconHome = QIcon(homeIcon_path)
        iconAdd = QIcon(addIcon_path)
        iconSetting = QIcon(settingIcon_path)
        iconProfile = QIcon(profileIcon_path)

        iconList = [iconHome, iconAdd, iconSetting, iconProfile]

        layout = QHBoxLayout()

        for i, icon in enumerate(iconList):
            button = QPushButton()
            button.setIcon(icon)
            button.setIconSize(QSize(35, 35))
            button.setFlat(True)
            button.setCheckable(True)
            button.clicked.connect(lambda _, index=i: self.stack.setCurrentIndex(index))
            button.setStyleSheet(f"""
                QPushButton{{
                    color: {TEXT['primary']};
                    background-color: transparent;
                }}
                QPushButton:hover{{
                    color: {COLOR['hover']};
                }}
            """)
            layout.addWidget(button)

        self.setLayout(layout)
