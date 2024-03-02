from flask  import Flask, json, request, jsonify, make_response
import pymysql
# ------------------------------------- 변수부 ---------------------------------------
host_num = '0.0.0.0' # flask 웹 서버의 host (localhost는 '0.0.0.0' 이나 '127.0.0.1' 으로 설정)
port_num = '5003' # flask 웹 서버의 port 번호

app = Flask(__name__)
# ------------------------------------- reference ---------------------------------------
# Figma : https://www.figma.com/file/kfLtLFwBUvNIiaNvlvvlHb/Wireframe-01?type=design&node-id=0-1&mode=design

# ------------------------------------- db connect --------------------------------------
# dbConnect.py # DB 연결 (mysql)
def dbcon():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='h96071212!', db='member', charset='utf8')
    if conn.open:
        print('데이터베이스에 연결되었습니다.')
    return conn

def dbclose(conn):
    conn.close()
# --------------------------------- chatting server ------------------------------------
# 주영 코드에서 작동 완료
# 앱(android studio)에서 채팅 데이터를 받아오는 작업
@app.route('/chatting', methods=['POST','GET'])
def chatting_server():    
    try:
        # Android studio -> flask 로 채팅 데이터 가져오기 (사용자 -> AI)
        chat_data = request.json['chat']
        print("채팅 : " + chat_data)
        # flask -> Android studio 로 채팅 보내기 (AI -> 사용자)
        # 여기에서 AI의 응답을 생성하고 안드로이드 앱으로 보내줄 수 있음
        ai_response = {"AIChating": "저는 AI에요. 무엇을 도와드릴까요?"}
        result = json.dumps(ai_response, ensure_ascii=False)
        res = make_response(result)
        res.headers['Content-Type'] = 'application/json'
        return res
    except KeyError:
        return make_response("Invalid JSON format or missing 'chat' key", 400)
# --------------------------------- userJoin, login ------------------------------------
# 회원가입 시 회원 가입 정보를 DB에 저장하는 코드
# android studio 'AndroidStudioconnect' 코드에서 정상 작동되는 것 확인 완료

# models.py # app.py(앱)에서 받아온 데이터들을 DB(mysql)에 추가한다.

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

#login(로그인) 페이지의 flask 서버 (login)
@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        login_id = request.json['login_id']
        # login_name = request.json['loginName']
        # login_birth = request.json['loginBrith']
        login_pw = request.json['login_pw']
        # login_phone_no = request.json['loginPhoneNo']
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

#userJoin(회원가입) 페이지의 flask 서버 (userJoin)
@app.route('/userJoin', methods=['POST', 'GET'])
def user_join():
    try:
        user_id = request.json['userID']
        # member_phone_no = request.json['memberPhoneNo']
        user_password = request.json['userPassword']
        # member_name = request.json['memberName']
        user_name = request.json['userName']
        # member_birth = request.json['memberBirth']
        # guardian_name = request.json['guardianName']
        # guardian_phone_no = request.json['guardianPhoneNo']
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
        return "앱(android studio)에서 데이터를 가져오는데 실패했습니다." # android studio의 Logcat에 전송되는 메시지

# ------------------------------ login ----------------------------------------

# ------------------------ flask web server running ------------------------------------
if __name__ == "__main__":
    app.run(host=host_num, port=port_num, debug=True)
			# port : 웹서버를 5003포트에서 실행하겠다는 설정