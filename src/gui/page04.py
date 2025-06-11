from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

### NOTICE! : add page

class page04(DefaultLayout):
     def __init__(self):
          super().__init__()
          self.infoWidget = inputInfo()
          self.wordListWidget = wordList()
          self.contentLayout.addWidget(self.infoWidget) 
          self.contentLayout.addWidget(self.wordListWidget)
          # 버튼set
          submitButton = QPushButton("submit")
          submitButton.clicked.connect(self.allSubmit)
          self.contentLayout.addWidget(submitButton)
     
     def allSubmit(self):
          title = self.infoWidget.getTitle()
          language = self.infoWidget.getLanguage()
          wordData = self.wordListWidget.getWordList()

          # 여기서 DB처리


class inputInfo(QWidget): 
     def __init__(self):
          super().__init__()
          layout = QVBoxLayout()

          self.titleInput = QLineEdit()
          self.titleInput.setPlaceholderText("title")
          self.title.setStyleSheet("border: none; border-bottom: 1px solid gray")

          self.languageInput = QLineEdit()
          self.languageInput.setPlaceholderText("language")
          self.languageInput.setStyleSheet("border: none; border-bottom: 1px solid gray")

          layout.addWidget(self.titleInput)
          layout.setSpacing(15) 
          layout.addWidget(self.languageInput)

     def getTitle(self):
          return self.titleEdit.text()

     def getLanguage(self):
          return self.languageEdit.text()


# 단어 저장 관리 클래스 - return을 위함
class wordList(QWidget):
     def __init__(self):
          super().__init__()
          self.inputIndex = 1
          self.wordList = []       # return vlaue 

          self.layout = QVBoxLayout()
          self.setLayout(self.layout)

          self.addInputRow()       # 입력창생성

     def addInputRow(self):
          row = wordInput(self.inputIndex, self.saveWord)
          self.layout.addWidget(row)
          self.inputIndex += 1

     def saveWord(self, word, meaning):
          self.wordList.append((word, meaning))
          self.addInputRow()

     def getWordList(self):
          return self.wordList
     

# input 창 관리 클래스
class wordInput(QWidget):
     def __init__(self, index: int, saveWord, addInput):
          super().__init__()
          self.saveWord = saveWord

          self.wordInput = QLineEdit()
          self.wordInput.setPlaceholderText = "word"
          self.meanInput = QLineEdit()
          self.meanInput.setPlaceholderText = "meaning"

          # 
          enterButton = QPushButton()
          enterButton.setIcon(QIcon("../assets/icons/iconEnter.png"))
          enterButton.setIconSize(QSize(23, 16))
          enterButton.setFlat(True) #배경 없애기
          enterButton.clicked.connect(submit)
          
          self.wordInput.returnPressed.connect(submit)
          self.meanInput.returnPressed.connect(submit)

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
          # horiz2.addwidget(QLabel()) #간격
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
                    self.saveWord(word, meaning)       # wordList class에 있는 메서드
