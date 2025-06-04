import sys
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


