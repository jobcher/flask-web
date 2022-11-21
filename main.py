"""
flask web
"""
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello,jobber'

app.run()