from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

### NOTICE! : wordList 상세 페이지 ->  word 복습

class page03_01(QWidget):
     def __init__(self):
          super().__init__()

          self.words = [
              ("apologize", "사과하다"),
              ("consider", "고려하다"),
              ("deliver", "배달하다")
          ]
          self.index = 0
          self.covered = False

          self.initUI()


     def initUI(self):
          layout = QVBoxLayout()

          # 카드
          self.wordCard = QWidget()
          self.wordCard.setStyleSheet(f"""
               background-color: {COLOR['secondary']};
               border-radius: 20px;
          """)
          cardLayout = QVBoxLayout()

          self.wordLabel = QLabel()
          self.wordLabel.setFont(QFont("Pretendard", 22))
          self.wordLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

          self.meaningLabel = QLabel()
          self.meaningLabel.setFont(QFont("Pretendard", 18))
          self.meaningLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

          self.checkBox = QCheckBox()
          self.checkBox.setFixedSize(20, 20)
          cbLayout = QHBoxLayout()
          cbLayout.addStretch()
          cbLayout.addWidget(self.checkBox)

          cardLayout.addWidget(self.wordLabel)
          cardLayout.addWidget(self.meaningLabel)
          cardLayout.addLayout(cbLayout)
          self.wordCard.setLayout(cardLayout)
          layout.addWidget(self.wordCard)

          # 버튼들 조합
          buttonLayout = QHBoxLayout()
          self.nextBtn = QPushButton(">")
          self.coverBtn = QPushButton("cover")
          self.soundBtn = QPushButton()
          self.soundBtn.setIcon(QIcon("../assets/icons/iconSound.svg"))

          for btn in (self.nextBtn, self.coverBtn, self.soundBtn):
               btn.setFixedSize(80, 40)
               btn.setStyleSheet(f"""
                    background-color: {COLOR['secondary']};
                    border-radius: 10px;
               """)
               buttonLayout.addWidget(btn)

          layout.addLayout(buttonLayout)
          self.setLayout(layout)
          self.updateCard()

          self.nextBtn.clicked.connect(self.showNextCard)
          self.coverBtn.clicked.connect(self.toggleCover)
          # self.soundBtn.clicked.connect(self.playSound)  # TTS 추후 추가 가능

     def updateCard(self):
          word, meaning = self.words[self.index]
          self.wordLabel.setText(word)
          self.meaningLabel.setText("" if self.covered else meaning)

     def showNextCard(self):
          self.index = (self.index + 1) % len(self.words)
          self.covered = False
          self.updateCard()

     def toggleCover(self):
          self.covered = not self.covered
          self.updateCard()

