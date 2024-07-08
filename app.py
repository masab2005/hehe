from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, MASAB!'
app.run(host='0.0.0.0', debug=True)