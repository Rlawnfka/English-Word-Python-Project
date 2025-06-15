from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

### NOTICE! : select title

class page02(QWidget):
     def __init__(self):
          super().__init__()
          mainLayout = QVBoxLayout(self)
          
          scroll = QScrollArea()
          scroll.setWidgetResizable(True)

          scrollContent = QWidget()
          self.setStyleSheet(f"""
               color: {TEXT['primary']};
          """)
          self.contentLayout = QVBoxLayout(scrollContent)
          
          #########################
          # DB 처리
          for i in range(4):
               info = createShowInfo("unit English", "2024/05/24", "English")
               self.contentLayout.addWidget(info)

          scroll.setWidget(scrollContent)
          mainLayout.addWidget(scroll)


#  만듭니다.
class createShowInfo(QWidget):
     def __init__(self, title : str, getdate:str, language: str):
          super().__init__()

          titleLabel = QLabel(title)
          titleLabel.setFont(QFont("Pretandard", 14, QFont.Weight.Bold))

          dateLabel = QLabel(getdate)
          languageLabel = QLabel(language)
          
          # 에러 발생 가능성
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

          



     

     