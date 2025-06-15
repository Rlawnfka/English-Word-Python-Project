from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from datetime import datetime

from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

from data.word_manager import *

import os
### NOTICE! : wordList 상세 페이지 & word 복습

class page03(QWidget):
     def __init__(self):
          super().__init__()
          self.contentLayout = QVBoxLayout()

          scroll = QScrollArea()
          scroll.setWidgetResizable(True)

          card = cardContainer()
          scroll.setWidget(card)

          self.contentLayout.addWidget(scroll)
          self.setLayout(self.contentLayout)

class cardContainer(QWidget):
     def __init__(self, words=None):
          super().__init__()

          outerLayout = QVBoxLayout()
          outerLayout.setContentsMargins(20,20,20,20)

          container = QWidget()
          container.setStyleSheet(f"""
            background-color: {COLOR['secondary']};
            border-radius: 20px;
          """)
          
          innerLayout = QVBoxLayout()
          innerLayout.setSpacing(15)
          innerLayout.setContentsMargins(20,20,20,20)

          innerLayout.addWidget(topWidget())
          innerLayout.addWidget(unknownWordButtons())
          innerLayout.addWidget(reviewProgressInfo())

          if words is None:
               words = ["apple", "banana", "cherry", "date","apple", "banana", "cherry", "date","apple"]
               # TODO : wordList 안늘어나는 문제 해결하기

          innerLayout.addWidget(WordLabels(words))

          container.setLayout(innerLayout)
          
          outerLayout.addWidget(container)

          self.setLayout(outerLayout)

class showTitleInfo(QWidget):
     def __init__(self, title: str, getdate: str, language: str):
          super().__init__()

          titleLabel = QLabel(title)
          titleLabel.setFont(QFont("Pretandard", 22, QFont.Weight.Bold))
          titleLabel.setStyleSheet(f"""
               color: {TEXT['primary']}
          """)

          dateLabel = QLabel(getdate)
          languageLabel = QLabel(" · "+language)
          dateLabel.setFont(QFont("Pretandard", 14))
          languageLabel.setFont(QFont("Pretandard", 14))

          textGrayBottom = QHBoxLayout()
          DateStyle = f"""
          QLabel {{
               color:{TEXT['secondary']};
               }}
          """
          LanguageStyle = f"""
          QLabel {{
               color:{TEXT['secondary']};
               margin-right:14px;
               }}
          """
          dateLabel.setStyleSheet(DateStyle)
          languageLabel.setStyleSheet(LanguageStyle)
          textGrayBottom.addWidget(dateLabel)
          textGrayBottom.addWidget(languageLabel)

          textLayout = QVBoxLayout()
          textLayout.addWidget(titleLabel)
          textLayout.addLayout(textGrayBottom)

          self.setLayout(textLayout)

class editRemoveButtons(QWidget):
     def __init__(self):
          super().__init__()

          # 수정 버튼
          editButton = QPushButton() 
          editIcon_path = os.path.join(os.path.dirname(__file__), "../assets/icons/editIcon.png")
          editButton.setIcon(QIcon(editIcon_path))
          editButton.setIconSize(QSize(32,32)) 
          # 창이 늘어나도 크기 변하지 않음
          editButton.setFixedSize(32,32) 
          # 다른 페이지로 이동
          editButton.clicked.connect(lambda:None) 

          # 삭제 버튼
          binButton = QPushButton() 
          binIcon_path = os.path.join(os.path.dirname(__file__), "../assets/icons/iconBin.png")
          binButton.setIcon(QIcon(binIcon_path))
          binButton.setIconSize(QSize(32,32))
          binButton.setFixedSize(32,32)
          binButton.clicked.connect(self.DeleteQeustion)

          # 수정버튼 + 삭제버튼
          buttons = QHBoxLayout()
          buttons.addWidget(editButton)
          buttons.addWidget(binButton)
          self.setLayout(buttons)

     def DeleteQeustion(self):
          reply = QMessageBox.question(
               self,
               "삭제 확인",
               "정말 삭제하시겠습니까?",
               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
          )

          if reply == QMessageBox.StandardButton.Yes:
               self.DeleteWordList()
          
     def DeleteWordList(self):
          # TODO : 삭제 로직 작성
          print("WordList deleted.")          

class topWidget(QWidget):
     def __init__(self):
          super().__init__()

          # 왼쪽 / 제목 + 날짜 + 언어
          titleInfo = showTitleInfo("Sample Title", "2025/06/14", "English")

          # 오른쪽 / 수정 버튼, 삭제 버튼
          modifyButtons = editRemoveButtons()

          # 전체 가로로 정렬하기
          topLayout = QHBoxLayout()
          topLayout.addWidget(titleInfo) # 왼쪽에 제목 
          topLayout.addStretch() # 가운데 공간 밀기
          topLayout.addWidget(modifyButtons, alignment=Qt.AlignmentFlag.AlignTop)  # 오른쪽에 버튼

          self.setLayout(topLayout)
     
class unknownWordButtons(QWidget): 
     def __init__(self):
          super().__init__()

          # f-string 쓸 때는 중괄호를 이중으로 {{}}
          buttonStyle = f"""
          QPushButton {{
               background-color: {COLOR['primary']};
               color:white;
               border:none;
               border-radius:12px;
               min-width:80px;
               min-height:32px;
               font-size:16px;
               font-weight:bold;
               }}
          QPushButton:hover {{
               background-color: {COLOR['hover']};
          }}
          """
 
          # REVIEW 버튼
          reviewButton = QPushButton("REVIEW")
          reviewButton.setStyleSheet(buttonStyle)
          reviewButton.clicked.connect(self.updateLastReview) 

          #STARED 버튼
          staredButton = QPushButton("STARED")
          staredButton.setStyleSheet(buttonStyle)
          staredButton.clicked.connect(lambda:None)

          buttons = QHBoxLayout() 
          buttons.addWidget(reviewButton)
          buttons.addWidget(staredButton)
          self.setLayout(buttons)

     # REVIEW 버튼 클릭하면 최근(오늘) 날짜 lastReviewed에 저장
     # 오늘 날짜 구하는 함수
     def updateLastReview(self):
          today = datetime.today().strftime("%Y/%m/%d")
          # DB에 lastReviewed 저장하는 코드 작성
          # lastreviewDate 바뀌어야 함

class LastReview(QWidget):
     def __init__(self):
          super().__init__()
          grayText = f""" 
               QLabel{{
               color:gray;
               }}
          """
          # last-review label
          lastViewLabel = QLabel("last-review")
          lastViewLabel.setFont(QFont("Pretandard", 14))
          lastViewLabel.setStyleSheet(grayText)
          # last-review date
          self.lastViewDate = QLabel("2025/6/15") # last-review 날짜 넣어야함
          self.lastViewDate.setFont(QFont("Pretandard", 17))
          # 세로 정렬
          lastLayout = QVBoxLayout()
          lastLayout.addWidget(lastViewLabel)
          lastLayout.addWidget(self.lastViewDate)

          self.setLayout(lastLayout)

class Reviewed(QWidget):
     def __init__(self):
          super().__init__()
          grayText = f""" 
               QLabel{{
               color:gray;
               }}
          """
          # reviewed label
          reviewedLabel = QLabel("reviewed")
          reviewedLabel.setFont(QFont("Pretandard", 14))
          reviewedLabel.setStyleSheet(grayText)
          # reviewed number
          self.reviewedNumber = QLabel("2025/6/15") # reviewed 날짜 넣어야함
          self.reviewedNumber.setFont(QFont("Pretandard", 17))
          # 세로 정렬
          reviewedLayout = QVBoxLayout()
          reviewedLayout.addWidget(reviewedLabel)
          reviewedLayout.addWidget(self.reviewedNumber)

          self.setLayout(reviewedLayout)

class Progress(QWidget):
     def __init__(self):
          super().__init__()
          grayText = f""" 
               QLabel{{
               color:gray;
               }}
          """
          # progress label
          progressLabel = QLabel("progress")
          progressLabel.setFont(QFont("Pretandard", 14,))
          progressLabel.setStyleSheet(grayText)
          # progress
          self.progressValue = QLabel("10/35") # 계산해서 넣어야함
          self.progressValue.setFont(QFont("Pretandard", 17))
          # 세로 정렬
          progressLayout = QVBoxLayout()
          progressLayout.addWidget(progressLabel)
          progressLayout.addWidget(self.progressValue)

          self.setLayout(progressLayout)

# TODO : 조회 저장 기능 구현
class reviewProgressInfo(QWidget):
     def __init__(self):
          super().__init__()

          lastReview = LastReview()
          reviewed = Reviewed()
          progress = Progress()

          reviewProgress = QHBoxLayout()
          reviewProgress.addWidget(lastReview)  
          reviewProgress.addStretch()
          reviewProgress.addWidget(reviewed)
          reviewProgress.addStretch()
          reviewProgress.addWidget(progress)

          self.setLayout(reviewProgress)

class WordLabels(QWidget):
     def __init__(self, words=None):
          super().__init__()
          # 단어 카드들 구현
         
          labelStyle = f"""
          QLabel {{
               background-color:white;
               border-radius: 8px;
               border: none;
               padding: 8px;
               font-size:16px;
               min-width: 100px;
               min-height:40px;
          }}
          """
          grid = QGridLayout()
          grid.setSpacing(10)

          for index, word in enumerate(words):
               label = QLabel(word)
               label.setStyleSheet(labelStyle)
               row = index // 2
               col = index % 2
               grid.addWidget(label, row, col)
          self.setLayout(grid)


