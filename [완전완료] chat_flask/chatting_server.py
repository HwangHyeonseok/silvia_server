# 주영 코드에서 작동 완료
# 앱(android studio)에서 데이터를 받아오는 작업
from flask  import Flask, json, request, jsonify, make_response

app = Flask(__name__)
# http://ip:5000/sendserver 주소가 호출되면 아래의 함수를 실행 (ip : 자신의 서버 ip)
@app.route('/chatting', methods=['POST','GET'])
def chatting_server():    
    try:
        # Android studio -> flask 로 채팅 데이터 가져오기 (사용자 -> AI)
        chatData = request.json['chat']
        print("채팅 : " + chatData)
        # flask -> Android studio 로 채팅 보내기 (AI -> 사용자)
        # 여기에서 AI의 응답을 생성하고 안드로이드 앱으로 보내줄 수 있음
        ai_response = {"AIChating": "저는 AI에요. 무엇을 도와드릴까요?"}
        result = json.dumps(ai_response, ensure_ascii=False)
        res = make_response(result)
        res.headers['Content-Type'] = 'application/json'
        return res
    except KeyError:
        return make_response("Invalid JSON format or missing 'chat' key", 400)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5003', debug=True)
			# port : 웹서버를 5003포트에서 실행하겠다는 설정