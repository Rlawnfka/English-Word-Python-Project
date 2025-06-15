from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefaultLayout import DefaultLayout
from data.word_manager import Titles
from defalut_setting.colors import *

### NOTICE! : select title 

class page02(QWidget):
     def __init__(self, db):
          super().__init__()
          mainLayout = QVBoxLayout(self)
          
          scroll = QScrollArea()
          scroll.setWidgetResizable(True)

          scrollContent = QWidget()
          self.setStyleSheet(f"""
               color: {TEXT['primary']};
          """)
          self.contentLayout = QVBoxLayout(scrollContent)


          # DB 연결
          self.db = db
          titleList = Titles(db).getTitles()

          # DB로 info 생성
          for title in titleList:
               collection = db[title]
               document = collection.find_one()

               if document:
                    date = document.get("firstDate", "").strftime("%Y/%m/%d")
                    language = document.get("language")
                    info = createShowInfo(title, date, language)
                    self.contentLayout.addWidget(info)

          # 콘텐츠를 스크롤 영역에 넣기
          scroll.setWidget(scrollContent)
          mainLayout.addWidget(scroll)

class createShowInfo(QWidget):
     def __init__(self, title : str, getdate:str, language: str):
          super().__init__()

          titleLabel = QLabel(title)
          titleLabel.setFont(QFont("Pretandard", 14, QFont.Weight.Bold))

          dateLabel = QLabel(getdate)
          languageLabel = QLabel(language)
          
          # 에러 발생 가능성 지움
          # bookLabel = QLabel("../assets/icons/iconBook.png") 

          # 날짜 + 언어 
          textGrayBottom = QHBoxLayout()
          textGrayBottom.addWidget(dateLabel)
          textGrayBottom.addWidget(languageLabel)

          # title + (날짜 + 언어)
          textLayout = QVBoxLayout()
          textLayout.addWidget(titleLabel)
          textLayout.addLayout(textGrayBottom)

          # + 아이콘
          layout = QHBoxLayout()
          layout.addLayout(textLayout)
          layout.addStretch()

          self.setLayout(layout)

          



     

     