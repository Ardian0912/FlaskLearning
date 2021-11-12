from flask import Flask
app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The Project Page'
@app.route('/about')
def about():
    return 'The about page'


