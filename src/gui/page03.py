from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefaultLayout import DefaultLayout

### NOTICE! : wordList 상세 페이지 & word 복습

class page03(DefaultLayout):
     def __init__(self):
          super().__init__()
          self.contentLayout.addWidget(categoryInfo())
          self.contentLayout.addWidget(unknownWordButtons())
          


class categoryInfo:
     def __init__(self):
          super().__init__()
          categoryTitle = QLabel("unit4 English")
          date = QLabel("2024/05/25"+" · "+"English") #날짜와 언어는 db에서 가져오기

class unknownWordButtons: # 버튼 좌우 수평 레이아웃
     def __init__(self):
          super().__init__()
          button_layout = QHBoxLayout() 
          reviewButton = QPushButton("REVIEW")
          reviewButton.clicked.connect()
          staredButton = QPushButton("STARED")
          staredButton.clicked.connect()

          button_layout.addStretch() # 오른쪽 정렬
          self.addWidget(reviewButton)
          self.addWidget(staredButton)


     