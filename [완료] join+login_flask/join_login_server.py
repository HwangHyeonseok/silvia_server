# 내 코드 AndroidStudioconnect 에서 작동 완료
import pymysql
host = '0.0.0.0' # 호스트 번호 설정 (localhost 루프백은 127.0.0.1이나 0.0.0.0)
port = 5000 # 포트 번호 설정 (android studio와 일치시킬 것)

# dbConnect.py # DB 연결 (mysql)
def dbcon():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='h96071212!', db='member', charset='utf8')
    if conn.open:
        print('데이터베이스에 연결되었습니다.')
    return conn

def dbclose(conn):
    conn.close()

# models.py # app.py(앱)에서 받아온 데이터들을 DB(mysql)에 추가한다.

import pymysql

class sendData():
    def sendtodb(self, id, password, name):
        conn = dbcon()
        data = (id, password, name)
        curdic = conn.cursor()
        sql = "INSERT INTO join_user VALUES(%s, %s, %s)"
        curdic.execute(sql, data)
        conn.commit()
        dbclose(conn)
        print("DB에 정상적으로 데이터를 추가했습니다.")
        return True  # 데이터 추가 성공

# app.py  # 앱(android studio)에서 데이터를 받아오는 작업
from flask import Flask, json, request

app = Flask(__name__)
sendDataInstance = sendData()  # sendData 클래스의 인스턴스 생성

#login(로그인) 페이지의 flask 서버
@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        login_id = request.json['login_id']
        login_pw = request.json['login_pw']
        print("id : " + login_id)
        print("password : " + login_pw)
        if login_id == "admin": # 현재 관리자 로그인은 임시적으로 admin
            print("관리자 로그인에 성공했습니다.")
            return json.dumps({"success": True})  # android studio에 로그인 성공 json 보내기
        else:
            return json.dumps({"success": False})  # android studio에 로그인 실패 json 보내기
    except Exception as e: # flask 코드 오류 시 예외처리
        print("[flask 코드 오류]", str(e))
        return json.dumps({"success": False})  # 예외 발생 시 로그인 실패 응답

#userJoin(회원가입) 페이지의 flask 서버
@app.route('/userJoin', methods=['POST', 'GET'])
def user_join():
    try:
        user_id = request.json['userID']
        user_password = request.json['userPassword']
        user_name = request.json['userName']
        print("id : " + user_id)
        print("password : " + user_password)
        print("name : " + user_name)
        success = sendDataInstance.sendtodb(user_id, user_password, user_name)
        if success:
            return "성공적으로 앱(android studio)에서 데이터를 가져왔습니다."
        else:
            return "데이터 추가 실패"
    except Exception as e:
        print("[flask 코드 오류]", str(e))
        return "앱(android studio)에서 데이터를 가져오는데 실패했습니다."

# runServer.py # 서버 실행 파일 (여기로 실행하면 된다.)
if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
