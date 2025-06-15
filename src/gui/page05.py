from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gui.DefaultLayout import DefaultLayout
from defalut_setting.colors import *

from data.word_manager import *

### NOTICE! : setting & 새 외부창 생성

# 설정 레이아웃을 한줄씩 넣어주는 함슈
def createSettingRow(label_text: str, setting_widget: QWidget) -> QHBoxLayout:
    row = QHBoxLayout()
    label = QLabel(label_text)
    label.setFixedWidth(150)
    row.addWidget(label)
    row.addWidget(setting_widget)
    return row

# page05 전체 구성
class page05(QWidget):
     def __init__(self, m_window, db):
          super().__init__()
        
          self.windows = m_window
          self.db = db
          self.titleList = Titles(db).getTitles()
        
          self.slideSpeed = SlideSpeed()
          self.colorPick = colorPick()
          self.wordSelect = wordSelect(self.db, self.titleList)
          self.displayTop = displayTop()
          self.keepAlive = KeepWindowAlive() 
          layout = QVBoxLayout()
          layout.addLayout(createSettingRow("창 생성", WindowControl(self, m_window)))
          layout.addLayout(createSettingRow("전원 꺼져도 창 유지", self.keepAlive))
          layout.addLayout(createSettingRow("카드 넘김 속도", self.slideSpeed))
          layout.addLayout(createSettingRow("창 색상 바꾸기", self.colorPick))
          layout.addLayout(createSettingRow("단어장 선택", self.wordSelect))
          layout.addLayout(createSettingRow("창 최상위 표시", self.displayTop))
          layout.addStretch()
          self.setLayout(layout)
          self.setStyleSheet(f"""
               color: {TEXT["primary"]}
          """)

     def getSlideSpeed(self):
         return self.slideSpeed.getValue()

     def getColor(self):
         return self.colorPick.getColor()

     def getSelected(self):
         return self.wordSelect.getWords()

     def isAlwaysOnTop(self):
         return self.displayTop.isChecked()

     def keepWindow(self):
        return self.keepAlive.isChecked()



# 창 생성삭삭제/page를통해 외부창으로 넘김
class WindowControl(QWidget):
     def __init__(self, page, m_window):
          super().__init__()
          self.parent = page
          self.m_window = m_window #이 페이지의 윈도우를 의미
          self.windows = self.m_window.windows

          layout = QHBoxLayout()
          self.createBtn = QPushButton("생성")
          self.deleteBtn = QPushButton("삭제")

          for btn in (self.createBtn, self.deleteBtn):
               btn.setFixedSize(100, 40)
               btn.setStyleSheet(f"""
                    QPushButton{{
                        background-color: {COLOR['secondary']};
                        border-radius: 15px;
                        font-weight: bold;
                    }}
               """)
               layout.addWidget(btn)
               self.createBtn.clicked.connect(self.createWindow)
               self.deleteBtn.clicked.connect(self.deleteWindow)

               self.setLayout(layout)
               self.newWindow = None

     def createWindow(self):
         if self.newWindow is None:
               try:
                    interval = self.parent.getSlideSpeed() * 100
                    color = self.parent.getColor()
                    words = self.parent.getSelected()
                    top = self.parent.isAlwaysOnTop()

                    self.newWindow = createWordWindow(words, interval, color, top)
                    self.newWindow.show()
                    self.windows.append(self.newWindow)

               except Exception as e:
                    print("외부창 생성 실패", e)

     def deleteWindow(self):
          if self.newWindow:
               self.newWindow.close()
               self.newWindow = None



class createWordWindow(QWidget):
     def __init__(self, word_list, interval_ms=3000, color="#ffffff", stay_on_top=True):
          super().__init__()
        
          self.word_list = word_list if word_list else ["(단어 없음)"]
          self.index = 0
          self.setStyleSheet(f"background-color: {color}; font-size: 24px;")
          self.label = QLabel(self.word_list[self.index], self)
          self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

          layout = QVBoxLayout()
          layout.addWidget(self.label)
          self.setLayout(layout)

        # 항상 위에 표시 이거왜 안돼냐.
          if stay_on_top:
               self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        # 타이머로 단어 순환
          self.timer = QTimer(self)
          self.timer.timeout.connect(self.nextWord)
          self.timer.start(interval_ms)  # 밀리초 단위

          self.setFixedSize(250, 150)
          self.setWindowTitle("Shorty! - 외부 단어장")

     def nextWord(self):
        # 다음 단어 인덱스로 이동
        self.index = (self.index + 1) % len(self.word_list)
        self.label.setText(self.word_list[self.index])



# TODO : 추후 자세구현
#      : 컴퓨터 전원이 켜지면 바로 실행될 수 있도록 구현
class KeepWindowAlive(QWidget):
     def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.checkbox = QCheckBox()
        layout.addWidget(self.checkbox, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout(layout)

     def isChecked(self):
        return self.checkbox.isChecked()



# 카드 넘김 속도
class SlideSpeed(QWidget):
     def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(1, 20)
        self.slider.setValue(10)
        layout.addWidget(self.slider)
        self.setLayout(layout)

     def getValue(self):
        return self.slider.value()
    



class colorPick(QWidget):
     def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()
        self.color = QColor("#ffffff")
        self.colorBtn = QPushButton("색상 선택")
        self.colorBtn.clicked.connect(self.openColorDialog)
        layout.addWidget(self.colorBtn)
        self.setLayout(layout)

     def openColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color
            self.setStyleSheet(f"background-color: {color.name()};")

     def getColor(self):
        return self.color.name()
    
# 외부창에 표시될단어장 선택살려줘
class wordSelect(QWidget):
     def __init__(self, db, titleList):
          super().__init__()

          self.db = db
          self.titleList = titleList

          layout = QHBoxLayout()
          self.combo = QComboBox()
          self.combo.addItems(self.titleList)
          layout.addWidget(self.combo)
          self.setLayout(layout)

     def getWords(self):
        select = self.combo.currentText()

     #    dummy_data = {
     #        "토익 단어장": ["abandon", "baggage", "candidate"],
     #        "수능 필수 어휘2": ["analyze", "compare", "define"],
     #        "영어회화 정리1": ["hello", "how are you", "thank you"]
     #    }
     #    return dummy_data.get(select, ["(단어 없음)"])

# 창 최상위 표시
class displayTop(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.checkbox = QCheckBox("최상위 표시")
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

    def isChecked(self):
        return self.checkbox.isChecked()



