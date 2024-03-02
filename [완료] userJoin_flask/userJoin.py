# 회원가입 시 회원 가입 정보를 DB에 저장하는 코드

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

import pymysql

class sendData():
    def sendtodb(id, password, name):
        conn = dbcon()
        data = (id, password, name)
        curdic = conn.cursor()
        sql = "INSERT INTO join_user VALUES(%s, %s, %s)"
        curdic.execute(sql, data)
        conn.commit()
        dbclose(conn)
        print("DB에 정상적으로 데이터를 추가했습니다.")

# app.py  # 앱(android studio)에서 데이터를 받아오는 작업

from flask import Flask, json, request

app = Flask(__name__)

@app.route('/userJoin', methods=['POST', 'GET'])
def toDB():
    id = request.json['userID']
    password = request.json['userPassword']
    name = request.json['userName']
    print("id : " + id)
    print("password : " + password)
    print("name : " + name)
    
    sendData.sendtodb(id, password, name)
    
    return "성공적으로 앱(android studio)에서 데이터를 가져왔습니다."

# runServer.py # 서버 실행 파일 (여기로 실행하면 된다.)

from flask import Flask

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
