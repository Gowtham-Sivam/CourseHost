from flask import Flask, request, jsonify
from flask_asgi import FlaskASGI
from waitress import serve

app = Flask(__name__)
asgi_app = FlaskASGI(app)

# API for addition
@asgi_app.route('/add', methods=['get'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 + num2
    return jsonify({'result': result})

# API for subtraction
@asgi_app.route('/subtract', methods=['get'])
def subtract():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 - num2
    return jsonify({'result': result})

# API for multiplication
@asgi_app.route('/multiply', methods=['get'])
def multiply():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 * num2
    return jsonify({'result': result})

# API for division
@asgi_app.route('/divide', methods=['get'])
def divide():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num2 == 0:
        return jsonify({'error': 'Division by zero'})
    result = num1 / num2
    return jsonify({'result': result})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=8080)
