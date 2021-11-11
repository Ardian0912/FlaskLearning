from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Index Page'

@app.route('/nama')
def routing():
    return 'Aransyah'