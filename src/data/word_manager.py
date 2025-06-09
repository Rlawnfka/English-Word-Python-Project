# DB나 데이터처리
# 데이터를 해당 파일에서 gui로 불러옴
import os
from pymongo import MongoClient
from dotenv import load_dotenv
# .env 파일의 환경 변수들 불러오기
load_dotenv()
# mongodb 비밀번호 가져오기
MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client["Titles"]

data = db["unit4 english"]
lan = data.find({"language":"english"})

for doc in lan:
    print(doc)
