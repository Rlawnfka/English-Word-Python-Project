# DB나 데이터처리
# 데이터를 해당 파일에서 gui로 불러옴
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# .env 파일의 환경 변수들 불러오기
load_dotenv()


class connectDB:
    def __init__(self):

        # mongodb 비밀번호 가져오기
        MONGO_URL = os.getenv("MONGO_URL")

        if not MONGO_URL:
            raise ValueError("환경변수 mongo_url이 설정되지 않음")
        
        self.client = MongoClient(MONGO_URL)
        self.db = self.client["Titles"] # 외부에서 접근 가능 (self.db)
        
    
    def close(self):
        self.client.close()
