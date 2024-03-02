# 로그인 시 android studio에서 데이터를 받아오고 아이디만 체크하여 무조건 로그인 시키기
# 지금은 임의의 아이디 비교 

# dbConnect.py # DB 연결 (mysql)
import pymysql

def dbcon():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='h96071212!', db='member', charset='utf8')
    if conn.open:
        print('데이터베이스에 연결되었습니다.')
    return conn

def dbclose(conn):
    conn.close()

# models.py # app.py(앱)에서 받아온 데이터들을 DB(mysql)에 추가한다.

# import pymysql

# class sendData():
#     def sendtodb(id, password, name):
#         conn = dbcon()
#         data = (id, password, name)
#         curdic = conn.cursor()
#         sql = "INSERT INTO join_user VALUES(%s, %s, %s)"
#         curdic.execute(sql, data)
#         conn.commit()
#         dbclose(conn)
#         print("DB에 정상적으로 데이터를 추가했습니다.")

# app.py  # 앱(android studio)에서 데이터를 받아오는 작업

from flask import Flask, json, request

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def toDB():
    try:
        login_id = request.json['login_id']
        login_pw = request.json['login_pw']
        # name = request.json['userName']
        print("id : " + login_id)
        print("password : " + login_pw)
        # print("name : " + name)
        if login_id == "admin":
            print("관리자 로그인에 성공했습니다.")
            return json.dumps({"success":True}) # android studio에 로그인 성공 json 보내기
        else:
            return json.dumps({"success": False})  # android studio에 로그인 실패 json 보내기
        
        # sendData.sendtodb(id, password, name)
    except Exception as e: # flask 코드 오류 시 
        print("[flask 코드 오류]", str(e))
        return json.dumps({"success": False})  # 예외 발생 시 로그인 실패 응답


# runServer.py # 서버 실행 파일 (여기로 실행하면 된다.)
from flask import Flask

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
