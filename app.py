from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.sort_keys = False # ustawienie sortowania kluczy na False, żeby była dokładnie taka sama, jak podana w przykładzie

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def my_page():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    return f"Hello, {name}!"

@app.route('/api/v1.0/predict')
def api():
    number1 = float(request.args.get('num1', 0))
    number2 = float(request.args.get('num2', 0))

    if number1 + number2 > 5.8:
        result = 1
    else:
        result = 0

    response = {
        "prediction": result,
        "features": {
            "num1": number1,
            "num2": number2
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()