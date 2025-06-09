from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefaultLayout import DefaultLayout

from ..data import word_manager as DATA
from data.word_manager import *

### NOTICE! : wordList 상세 페이지 & word 복습

class page03(DefaultLayout):
     def __init__(self):
          super().__init__()
          self.contentLayout.addWidget(categoryInfo())
          self.contentLayout.addWidget(unknownWordButtons())
          
class categoryInfo:
     def __init__(self):
          super().__init__()

          
          # db에서 가져온 정보들
          language = DATA.doc["language"] 
          firstDate = DATA.onlyDate

          categoryTitle = QLabel("unit4 English")
          date = QLabel(firstDate+" · "+language) #날짜와 언어는 db에서 가져오기

          self.setWidget(categoryTitle)
          self.setWidget(date)

class editRemoveButtons:
     def __init__(self):
          super().__init__()

          layout = QHBoxLayout()

          self.editButton = QPushButton()
          self.editButton.setIcon(QIcon("/src/assets/icons/editIcon.png"))
          self.editButton.setIconSize(32,32) 
          self.editButton.setFixedSize(32,32) # 창이 늘어나도 크기 변하지 않음
          self.editButton.clicked.connect() # page03_01.py로 이동

          self.binButton = QPushButton()
          self.binButton.setIcon(QIcon("/src/assets/icons/iconBin.png"))
          self.binButton.setIconSize(32,32)
          self.binButton.setFixedSize(32,32)
          self.binButton.clicked.connect()

          layout.addStretch() # 오른쪽 정렬
          layout.addWidget(self.editButton)
          layout.addWidget(self.binButton)

class unknownWordButtons: 
     def __init__(self):
          super().__init__()
          layout = QHBoxLayout() 
          reviewButton = QPushButton("REVIEW")
          reviewButton.clicked.connect()
          staredButton = QPushButton("STARED")
          staredButton.clicked.connect()

          layout.addStretch() # 오른쪽 정렬
          self.addWidget(reviewButton)
          self.addWidget(staredButton)


     