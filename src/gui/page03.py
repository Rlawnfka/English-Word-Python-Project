from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from datetime import datetime

from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

from ..data import word_manager as DATA
from data.word_manager import *

### NOTICE! : wordList 상세 페이지 & word 복습

class page03(DefaultLayout):
     def __init__(self):
          super().__init__()
          self.contentLayout.addWidget(topWidget())
          self.contentLayout.addWidget(unknownWordButtons())

class showTitleInfo(QWidget):
     def __init__(self, title: str, getdate: str, language: str):
          super().__init__()

          titleLabel = QLabel(title)
          titleLabel.setFont(QFont("Pretandard", 30, QFont.Weight.Bold))

          dateLabel = QLabel(getdate)
          languageLabel = QLabel(" · "+language)
          dateLabel.setFont(QFont("Pretandard", 17, QFont.Weight.Normal))
          languageLabel.setFont(QFont("Pretandard", 17, QFont.Weight.Normal))

          textGrayBottom = QHBoxLayout()
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
          editButton.setIcon(QIcon("/src/assets/icons/editIcon.png"))
          editButton.setIconSize(QSize(32,32)) 
          # 창이 늘어나도 크기 변하지 않음
          editButton.setFixedSize(32,32) 
          # 다른 페이지로 이동
          editButton.clicked.connect(lambda:None) 

          # 삭제 버튼
          binButton = QPushButton() 
          binButton.setIcon(QIcon("/src/assets/icons/iconBin.png"))
          binButton.setIconSize(QSize(32,32))
          binButton.setFixedSize(32,32)
          binButton.clicked.connect(lambda:None)

          # 수정버튼 + 삭제버튼
          buttons = QHBoxLayout()
          buttons.addWidget(editButton)
          buttons.addWidget(binButton)

          self.setLayout(buttons)

class topWidget(QWidget):
     def __init__(self):
          super().__init__()

          # 왼쪽 / 제목 + 날짜 + 언어
          titleInfo = showTitleInfo(DATA.getTitle, DATA.getDate, DATA.getLanguage)

          # 오른쪽 / 수정 버튼, 삭제 버튼
          modifyButtons = editRemoveButtons()

          # 전체 가로로 정렬하기
          topLayout = QHBoxLayout()
          topLayout.addWidget(titleInfo) # 왼쪽에 제목 
          topLayout.addStretch() # 가운데 공간 밀기
          topLayout.addWidget(modifyButtons)  # 오른쪽에 버튼

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
               padding:8px 24px;
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

class lastReviewClass(QWidget):
     def __init__(self):
          super().__init__()
          
          # last-review label
          lastViewLabel = QLabel("last-review")
          lastViewLabel.setFont(QFont("Pretandard", 15, QFont.Weight.Normal))
          # last-review date
          self.lastViewDate = QLabel() # last-review 날짜 넣어야함
          self.lastViewDate.setFont(QFont("Pretandard", 20, QFont.Weight.Normal))
          # 세로 정렬
          lastLayout = QVBoxLayout()
          lastLayout.addWidget(lastViewLabel)
          lastLayout.addWidget(self.lastViewDate)

          self.setLayout(lastLayout)

class ReviewedClass(QWidget):
     def __init__(self):
          super().__init__()

          # reviewed label
          reviewedLabel = QLabel("reviewed")
          reviewedLabel.setFont(QFont("Pretandard", 15, QFont.Weight.Normal))
          # reviewed number
          self.reviewedNumber = QLabel() # reviewed 날짜 넣어야함
          self.reviewedNumber.setFont(QFont("Pretandard", 20, QFont.Weight.Normal))
          # 세로 정렬
          reviewedLayout = QVBoxLayout()
          reviewedLayout.addWidget(reviewedLabel)
          reviewedLayout.addWidget(self.reviewedNumber)

          self.setLayout(reviewedLayout)

class ProgressClass(QWidget):
     def __init__(self):
          super().__init__()

          # progress label
          progressLabel = QLabel("progress")
          progressLabel.setFont(QFont("Pretandard", 15, QFont.Weight.Normal))
          # progress
          self.progressValue = QLabel() # 계산해서 넣어야함
          self.progressValue.setFont(QFont("Pretandard", 20, QFont.Weight.Normal))
          # 세로 정렬
          progressLayout = QVBoxLayout()
          progressLayout.addWidget(progressLabel)
          progressLayout.addWidget(self.progressValue)

          self.setLayout(progressLayout)

# TODO : 조회 저장 기능 구현
class reviewProgressInfo(QWidget):
     def __init__(self):
          super().__init__()

          lastReview = lastReviewClass()
          reviewed = ReviewedClass()
          progress = ProgressClass()

          reviewProgress = QHBoxLayout()
          reviewProgress.addWidget(lastReview)  
          reviewProgress.addStretch()
          reviewProgress.addWidget(reviewed)
          reviewProgress.addStretch()
          reviewProgress.addWidget(progress)

          self.setLayout(reviewProgress)

class WordLabels(QLabel):
     def __init__(self):
          super().__init__()

          # 단어 카드들 구현
