from flask import Flask
app = Flask(__name__)

@app.route('/projects/')
def show_user_profile(username):
    return 'Project Page'