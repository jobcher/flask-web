"""
flask web
"""
from flask import Flask

app = Flask(__name__)
# 导入配置文件
app.config.from_object('config')


# 解释路由
@app.route('/')
def hello():
    return 'hello,jobcher'

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=80)