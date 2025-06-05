import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import defalut

### NOTICE! : home, main page

class page01(QMainWindow):
     def __init__(self):
          super().__init__()
          self.initUI()

     def initUI():
          # 다른 요소에 대한 의존성
          defalutLayout = defalut()

     # 레이아웃, 스타일시트 
     pass



class setTopSentanse(QWidget):
     def __init__(self):
          super().__init__()
     
     # 문장을 DB에서 추출
     # 
     temp = "안녕하세요! Shorty입니다 😊\n단어, 짧은 복습 어떠신가요?"

     sentanse = QLabel(temp)
     font = QFont("Do Hyeon",25,QFont.Weight.regular)
     sentanse.setFont(font)

class setStartButton(QPushButton):
     pass

class setCategories(QWidget):
     pass

class setQuizBox(QWidget):
     def __init__(self):
          super().__init__()
          self.initUI()

     def initUI(self):
          quizTitle = QLabel("깜짝 퀴즈 ✅") # 이모티콘 미지원시 아이콘 이미지로 대체
          quizTitle.setFont(QFont("Do Hyeon", 25, QFont.Weight.reqular))

