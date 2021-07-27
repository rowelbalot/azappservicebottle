from bottle import Bottle, run

app = Bottle()

@app.route('/')
def hello():
    return "Hello Bottle!"

run(app,Port=80)
