from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

### NOTICE! : select title

class page02(QWidget):
     def __init__(self):
          super().__init__()
          # 전체 레이아웃
          mainLayout = QVBoxLayout(self)
          
          # 스크롤 영역
          scroll = QScrollArea()
          scroll.setWidgetResizable(True)

          # 스크롤 내부에 넣을 콘텐츠 위젯 생성
          scrollContent = QWidget()
          self.contentLayout = QVBoxLayout(scrollContent)

          # DB에서 삽입
          for i in range(4):
               info = createShowInfo("unit English", "2024/05/24", "English")
               self.contentLayout.addWidget(info)

          # 플러스 버튼 추가
          self.contentLayout.addWidget(info.createPlusBtn())


          # 콘텐츠를 스크롤 영역에 넣기
          scroll.setWidget(scrollContent)

          # 메인에 스크롤 추가
          mainLayout.addWidget(scroll)


class createShowInfo(QWidget):
     def __init__(self, title: str, getdate:str, language: str):
          super().__init__()

          titleLabel = QLabel(title)
          titleLabel.setFont(QFont("Pretandard", 14, QFont.Weight.Bold))

          dateLabel = QLabel(getdate)
          languageLabel = QLabel(language)

          bookLabel = QLabel("../assets/icons/iconBook.png")

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

          

     def createPlusBtn(self) -> QWidget:
          rtnWidget = QWidget()
          layout = QVBoxLayout()
          plusButton = QPushButton("+")
          plusButton .setFixedSize(60,60)
          plusButton.setStyleSheet(f"""
               background-color: {BACKGROUND['main']};
               font-size: 25px;
               border-radius: 10px;
          """)

          layout.addWidget(plusButton)
          rtnWidget.setLayout(layout)
          return rtnWidget
          

     

     