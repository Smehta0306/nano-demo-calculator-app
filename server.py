from flask import Flask,request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    request_data = request.json
    first = request_data.get("first", 0)
    second = request_data.get("second", 0)
    result = first + second
    return {"result": result}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    request_data = request.json
    first = request_data.get("first", 0)
    second = request_data.get("second", 0)
    result = first - second
    return {"result": result}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
