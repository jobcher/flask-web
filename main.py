"""
flask web
"""
from flask import Flask
from helper import is_isbn_or_key

app = Flask(__name__)
# 导入配置文件
app.config.from_object('config')


# 解释路由
@app.route('/book/search/<q>/<page>')
def search(q,page):
    """
        q:普通搜索 isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=80)
