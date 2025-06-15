from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from datetime import datetime

from data.word_manager import ConnectDB
from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

### NOTICE! : add page

class page04(QWidget):
     def __init__(self):
          super().__init__()

          self.connectDB = ConnectDB()
          self.db = self.connectDB.db # DB연결

          self.contentLayout = QVBoxLayout()
          self.setLayout(self.contentLayout)
          self.infoWidget = inputInfo()
          self.wordListWidget = wordList()
          self.contentLayout.addWidget(self.infoWidget) 
          self.contentLayout.addWidget(self.wordListWidget)
          self.setStyleSheet(f"""color:{TEXT['primary']}""")
          # 버튼set
          submitButton = QPushButton("submit")
          submitButton.clicked.connect(self.allSubmit)
          self.contentLayout.addWidget(submitButton)
     
     def allSubmit(self):
          
          

          title = self.infoWidget.getTitle().strip()
          language = self.infoWidget.getLanguage().strip()
          wordData = self.wordListWidget.getWordList()
          
          #컬렉션이름 = 제목
          collection = self.db[title] 
          wordDataList = []
          for w,m,u in wordData:
               # 각 리스트안에 있는 것들을 w,m,u으로 분리해서 딕셔너리로 변환
               wordDataList.append({
                    "word":w,
                    "meaning": m,
                    "unknown": u
               })     
          # 컬렉션에 넣을 데이터
          document = {
               "language": language,
               "firstDate": datetime.now(),
               "lastReviewDate": datetime.now(),
               "wordData": wordDataList
          }
          # 컬렉션에 데이터 하나 삽입
          collection.insert_one(document)

          self.connectDB.client.close()

class inputInfo(QWidget): 
     def __init__(self):
          super().__init__()
          layout = QVBoxLayout()

          self.titleInput = QLineEdit()
          self.titleInput.setPlaceholderText("title")
          self.titleInput.setStyleSheet("border: none; border-bottom: 1px solid gray")

          self.languageInput = QLineEdit()
          self.languageInput.setPlaceholderText("language")
          self.languageInput.setStyleSheet("border: none; border-bottom: 1px solid gray")

          layout.addWidget(self.titleInput)
          layout.setSpacing(15) 
          layout.addWidget(self.languageInput)
          self.setLayout(layout)

     def getTitle(self):
          return self.titleInput.text()

     def getLanguage(self):
          return self.languageInput.text()


# 단어 저장 관리 클래스 - return을 위함
class wordList(QWidget):
     def __init__(self):
          super().__init__()
          self.inputIndex = 1
          self.wordList = []       # return value 

          self.layout = QVBoxLayout()
          self.setLayout(self.layout)

          self.addInputRow()       # 입력창생성

     def addInputRow(self):
          row = wordInput(self.inputIndex, self.saveWord)
          self.layout.addWidget(row)
          self.inputIndex += 1

     def saveWord(self, word, meaning, unknown):
          self.wordList.append([word, meaning, unknown])
          self.addInputRow()

     def getWordList(self):
          return self.wordList
     

# input 창 관리 클래스
class wordInput(QWidget):
     def __init__(self, index: int, saveWord): # def __init__(self, index: int, saveWord, addInput):
          super().__init__()
          self.saveWord = saveWord

          self.wordInput = QLineEdit()
          self.wordInput.setPlaceholderText("word")
          self.meanInput = QLineEdit()
          self.meanInput.setPlaceholderText("meaning")

          # 
          enterButton = QPushButton()
          enterButton.setIcon(QIcon("../assets/icons/iconEnter.png"))
          enterButton.setIconSize(QSize(23, 16))
          enterButton.setFlat(True) #배경 없애기
          enterButton.clicked.connect(self.submit)
          
          self.wordInput.returnPressed.connect(self.submit)
          self.meanInput.returnPressed.connect(self.submit)

          deleteButton = QPushButton()
          deleteButton.setIcon(QIcon("../assets/icons/iconBin.png"))
          deleteButton.setIconSize(QSize(23,27))
          deleteButton.setFlat(True)

          # layout
          horiz1 = QHBoxLayout()   # 각 인풋을 반씩 나누어 합친다음 위아래로
          horiz2 = QHBoxLayout() 
          horiz1.addWidget(QLabel(str(index)))
          horiz1.addWidget(self.wordInput)
          horiz1.addWidget(deleteButton)
          # horiz2.addWidget(QLabel()) #간격
          horiz2.addWidget(self.meanInput)
          horiz2.addWidget(enterButton)

          layout = QVBoxLayout()
          layout.addLayout(horiz1)
          layout.addLayout(horiz2)
          self.setLayout(layout)

     def submit(self):
          word = self.wordInput.text()
          meaning = self.meanInput.text()
          if word and meaning:
               self.saveWord(word, meaning, True) # wordList class에 있는 메서드
