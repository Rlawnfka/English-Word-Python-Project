import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefalutLayout import DefalutLayout

### NOTICE! : home, main page

class page01(DefalutLayout):
     def __init__(self):
          super().__init__()

          self.contentLayout.addWidget(setTopSentanse())


class setTopSentanse(QWidget):
     def __init__(self):
          super().__init__()
     
          # temp의 문장을 DB에서 추출
          temp = "안녕하세요! Shorty입니다 😊\n단어, 짧은 복습 어떠신가요?"
          sentanse = QLabel(temp)

          font = QFont("Do Hyeon",25,QFont.Weight.regular)
          sentanse.setFont(font)

          layout = QVBoxLayout()
          layout.addWidget(sentanse)

          self.setLayout(layout)
          


class setStartButton(QPushButton):
     pass


class setCategories(QWidget):
     pass

class setQuizBox(QWidget):
     def __init__(self):
          super().__init__()
          layout = QVBoxLayout()
          self.setLayout(layout)

          word = "temporal"
          wordLayout = QLayout(word)
          # wordLayout.setStyleSheet()

          self.setStyleSheet("""
               background-color: color['secondary'];
               border-radius: 20px;          
          """)



