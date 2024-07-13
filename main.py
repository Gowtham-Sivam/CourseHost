from fastapi import FastAPI

app = FastAPI()

@app.get('/add')
def add(num1: int, num2: int):
    return {'result': num1 + num2}

@app.get('/subtract')
def subtract(num1: int, num2: int):
    return {'result': num1 - num2}

@app.get('/multiply')
def multiply(num1: int, num2: int):
    return {'result': num1 * num2}

@app.get('/divide')
def divide(num1: int, num2: int):
    if num2 == 0:
        return {'error': 'Division by zero'}
    return {'result': num1 / num2}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
