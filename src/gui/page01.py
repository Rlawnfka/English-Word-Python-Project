import sys
from util.importQt import *

'''
 NOTICE! : home, main page
### TODO : quixBox에 클릭된 버튼 정답 확인 로직

'''

class page01(DefaultLayout):
     def __init__(self, stack):
          super().__init__(stack)
          self.contentLayout.addWidget(setTopSentanse())
          self.contentLayout.addWidget(setStartButton())
          self.contentLayout.addWidget(setCategories())
          self.contentLayout.addWidget(setQuizBox())


class setTopSentanse(QWidget):
     def __init__(self):
          super().__init__()
     
          # temp의 문장을 DB에서 추출
          # 랜덤으로 바뀜
          temp = "안녕하세요! Shorty입니다 😊\n단어, 짧은 복습 어떠신가요?"
          sentanse = QLabel(temp)
          sentanse.setFont(QFont("Do Hyeon", 25, QFont.Weight.Normal))

          layout = QVBoxLayout()
          layout.addWidget(sentanse)

          self.setLayout(layout)



class setStartButton(QWidget):
     def __init__(self):
          super().__init__()
          startButton = QPushButton("START")
          startButton.setFixedHeight(60)
          startButton.setFixedWidth(250)
          # startButton.setFixedSize(60, 250)

          startButton.setStyleSheet(f"""
               QPushButton{{
                    background-color: {COLOR['primary']};
                    color: white;
                    font-size: 25px;                
                    border-radius: 15px;                    
               }}
               QPushButton:hover {{
                    background-color: {COLOR['secondary']};
               }}               
          """)
          # 페이지 만든 후 버튼 연결
          # startButton.clicked.connect(fn)
          layout = QVBoxLayout()
          layout.addWidget(startButton, alignment=Qt.AlignmentFlag.AlignCenter)
          self.setLayout(layout)


class setCategories(QWidget):
     def __init__(self):
          super().__init__()

          # DB에서 가장 최근(날짜기준)에 학습한 3개의 단어장 제목 가져오기
          # 현재 배열은 임시
          recentTitle = ["토익 단어장", "수능 필수 어휘2", "영어회화 학원 정리1 5월 29일"]
          
          layout = QVBoxLayout()
          
          for title in recentTitle:
               # 조건 : 긴 문자열 처리, 12문자 이상은 잘라버림 
               if len(title) >= 12:
                    currentTitle = title[:10] + ".."
               else:
                    currentTitle = title
               button = QPushButton(currentTitle)
               button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
               button.setStyleSheet(f"""
                    QPushButton{{
                         font-size: 15px;
                         border-radius: 10px;
                         background-color:{COLOR['secondary']};
                         color: {TEXT['secondary']};
                    }}
                    QPushButton:hover{{
                         background-color: {COLOR['nav']};
                    }}
               """)
               layout.addWidget(button)
          self.setLayout(layout)


# 피그마에 나와있는 순 (위  ~  아래로 읽으세요..)
class setQuizBox(QWidget):
     def __init__(self):
          super().__init__()

          layout = QVBoxLayout()
          layout.setSpacing(15) 
          # layout.setContentsMargins(20)

          quizTitle = QLabel("복습 퀴즈 ✅")
          quizTitle.setStyleSheet("font-size: 17px;")
          quizTitle.setFont(QFont("Do Hyeon", 25, QFont.Weight.Normal))
          
          # DB에서 랜덤으로 뽑아오기
          currentWord = "temporal"
          word = QLabel(currentWord)
          word.setFont(QFont("Pretandard", 25, QFont.Weight.DemiBold))
          layout.addWidget(word)

          selectlength = 3 # 선지가 3개
          for i in range(1, selectlength+1):
               layout.addWidget(self.createChoice(i, "임시"+str(i)))
          
          self.setStyleSheet(f"background-color: {COLOR['secondary']}; border-radius:20px;")
          self.setLayout(layout)


     # 선지 하나씩 만들어주는 메서드 
     def createChoice(self, index: int, meaning: str) -> QWidget:
          returnWidget = QWidget()
          layout = QHBoxLayout()
          layout.setSpacing(15) 

          # 네모 숫자
          number = QLabel(str(index))
          number.setFixedSize(35, 35)
          number.setAlignment(Qt.AlignmentFlag.AlignCenter)
          number.setStyleSheet(f"""
               background-color: {COLOR['secondary']};
               border-radius: 5px;
               color: {TEXT['secondary']};    
               padding: 10px;           
          """)

          # 버튼 (선지 막대기)
          button = QPushButton(meaning)
          button.setStyleSheet(f"""
               QPushButton{{
                    color: {TEXT['secondary']};
                    background-color: white;
                    border-radius: 10px;
                    text-align: left;
                    padding: 5px;
               }}
               QPushButton:hover{{
                    background-color: {BACKGROUND['card-hover']}
               }}
          """)

          #합체
          layout.addWidget(number)
          layout.addWidget(button)
          returnWidget.setLayout(layout)
          return returnWidget
     