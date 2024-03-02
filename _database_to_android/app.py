import pymysql
from flask import Flask, jsonify, make_response
import datetime, json

conn = pymysql.connect(host='localhost', user='root', password='h96071212!', db='MEMBER', charset='utf8') # mysql 연결
curs = conn.cursor() # sql문을 입력할 cursor 생성

if conn.open: # DB 연결 여부 확인
    print('연결되었습니다.')
try:
    app = Flask(__name__) # flask 앱 선언
    app.config['JSON_AS_ASCII'] = False # flask response 한글 깨짐 현상 방지
    # flask 메인 
    # __name__: 현재 이 파일을 실행하고 있는 파일의 이름이 들어감(원본과 같은 파일 일 경우 '__main__')

    @app.route('/test',methods=['POST','GET']) 
    # route() : 외부 웹브라우져에서 웹서버로 접근 시 해당 주소로 입력을 하게 되면 특정 함수가 실행되게 도와줌('/test': /test 주소에 접근하면 아래 함수 실행)
    def dbToWeb(): # DB에서 웹으로 데이터를 보내기위한 함수
            sql = "select * from member.USER" # DB에서 필요한 데이터 select하는 sql문
            curs.execute(sql) # sql문 실행
            rows = curs.fetchall() # select한 데이터 fetch (fetchall() : 모든 데이터 fetch)
            print(rows)
            return make_response(json.dumps(rows,ensure_ascii=False))
            # fetch한 데이터 json형식으로 변환 후 string으로 바꿔서 return

finally:
    app.run(host='0.0.0.0', port=5001) # 웹서버 호스트, 포트 지정
    conn.close() # DB 연결 해제