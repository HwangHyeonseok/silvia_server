# app.py(앱)에서 받아온 데이터들을 DB(mysql)에 추가한다.
import pymysql
from dbConnect import dbcon, dbclose

class sendData():
    def sendtodb(id,password,name):
        conn = dbcon() # db연결 함수
        data = (id,password,name) # 데이터 튜플형식으로 변경
        curdic = conn.cursor() # sql문을 입력할 cursor 생성
        sql = "INSERT INTO join_user VALUES(%s,%s,%s)" # [★] sql문
        curdic.execute(sql, data) # sql문 실행
        conn.commit() # 수정사항 반영
        dbclose(conn) # DB 연결 해제
        return print("DB에 정상적으로 데이터를 추가했습니다.")