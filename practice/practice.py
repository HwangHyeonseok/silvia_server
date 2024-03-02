from flask import Flask, jsonify

app = Flask(__name__) # flask 객체 생성 (app)

def add_file(data):
    return data+5

# routing 
@app.route("/")
def hi(): # hi 함수 자동 실행 
    return "<h2>fucking</h2>"

@app.route("/hello")
def hi_flask(): # 수정
    return "<h1>Hello Flask222!</h1>"

@app.route("/first/<username>") # username은 string 형만 가능 (int, float, string 모든 경우에서 사용할 수 있다.)
def get_first(username):
    return "<h3>Hello " + username + "!</h3>"

@app.route("/profile/<int:username>") # username은 int 형만 가능
def get_profile(username):
    return "<h2>profile: %d" % username # %d : int, %f : float, %s : string

@app.route("/second/<int:messageid>")
def get_second(messageid):
    data = add_file(messageid)
    return "<h1>%d</h1>" % (data)

@app.route('/json_test')
def hello_json():
    data = {'name' : '황현석', 'university' : 'sungkyul'}
    return jsonify(data)

if __name__ == "__main__": # 해당 python 파일에서 실행한거면
    app.run(host="127.0.0.1", port="8082") # app 객체의 flask 서버를 구동해라