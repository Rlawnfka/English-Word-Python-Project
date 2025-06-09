from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

### NOTICE! : select title

class page02(DefaultLayout):
     def __init__(self):
          super().__init__()

          # DB에서 삽입
          for i in range(4):
               info = createShowInfo("unit English", "2024/05/24", "English")
               self.contentLayout.addWidget(info)
          self.contentLayout.addWidget(info.createPlusBtn())


class createShowInfo(QWidget):
     def __init__(self, title: str, getdate:str, language: str):
          super().__init__()

          titleLabel = QLabel(title)
          titleLabel.setFont(QFont("Pretandard", 14, QFont.Weight.Bold))

          dateLabel = QLabel(getdate)
          languageLable = QLabel(language)

          bookLabel = QLabel("../assets/icons/iconBook.png")

          # 날짜 + 언어 
          textGrayBottom = QHBoxLayout()
          textGrayBottom.addWidget(dateLabel)
          textGrayBottom.addWidget(languageLable)

          # title + (날짜 + 언어)
          textLayout = QVBoxLayout()
          textLayout.addWidget(titleLabel)
          textLayout.addLayout(textGrayBottom)

          # + 아이콘
          layout = QHBoxLayout()
          layout.addLayout(textLayout)
          layout.addStretch()

          

     def createPlusBtn() -> QWidget:
          rtnWidget = QWidget()
          layout = QBoxLayout()
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
          

     

     