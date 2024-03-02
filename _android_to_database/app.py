# 앱(android studio)에서 데이터를 받아오는 작업

from flask  import Flask, json, request
from models import sendData

app = Flask(__name__)

@app.route('/sendserver', methods=['POST','GET'])
# http://ip:5000/sendserver 주소가 호출되면 아래의 함수를 실행 (ip : 자신의 서버 ip)
def toDB(): # DB에 저장 (android studio에서 데이터를 가져온다.)
    id = request.json['userID'] # [Android Studio - AndroidStudioconnect - Mainactivity.java] json형태의 키값중 'userID'의 값을 리턴
    password = request.json['userPassword'] # json형태의 키값중 'userPassword'의 값을 리턴
    name = request.json['userName'] # json형태의 키값중 'userName'의 값을 리턴
    print("id : " + id) 
    print("password : " + password)
    print("name : " + name)
    # request.json['key'] : 요청받은 json데이터에서 원하는 key의 값을 가져오는 메소드
    
    sendData.sendtodb(id,password,name) # models.py의 sendData클래스 내의 sendtodb함수 실행
    
    return "성공적으로 앱(android studio)에서 데이터를 가져왔습니다."