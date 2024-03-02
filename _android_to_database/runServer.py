# 서버 실행 파일 (여기로 실행하면 된다.)
from flask import Flask
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
			# port : 웹서버를 5000포트에서 실행하겠다는 설정