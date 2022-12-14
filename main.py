"""
flask web
"""

from flask import Flask, jsonify
from helper import is_isbn_or_key
from search import Search

app = Flask(__name__)
# 导入配置文件
app.config.from_object('config')


# 解释路由
@app.route('/search/<q>/<page>')
def search(q, page):
    """
        q:普通搜索 isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = Search.search_by_isbn(q)
    else:
        result = Search.search_by_keyword(q)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=80)
