# DB나 데이터처리
# 데이터를 해당 파일에서 gui로 불러옴
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# .env 파일의 환경 변수들 불러오기
load_dotenv()

class ConnectDB:
    def __init__(self):

        # env파일 안에 넣어둔 mongodb 비밀번호 가져오기
        MONGO_URL = os.getenv("MONGO_URL")

        self.client = MongoClient(MONGO_URL)
        self.db = self.client["Titles"]
        
    def close(self):
        self.client.close()

class Titles:
    def __init__(self, db):
        self.db = db

    def getTitles(self):
        return self.db.list_collection_names()
        
