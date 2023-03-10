"""
flask web
"""

from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)
# 导入配置文件
app.config.from_object('config')

# 连接数据库
db = pymysql.connect(host=app.config['DBHOST'],
                     user=app.config['DBUSER'],
                     password=app.config['DBPASSWORD'],
                     database=app.config['DBDATABASE'])

cursor = db.cursor()

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 处理搜索请求
@app.route('/search', methods=['POST'])
def search():
    # 获取搜索关键字
    keyword = request.form['keyword']
    # 执行MySQL查询
    cursor.execute("SELECT * FROM tianyi WHERE title LIKE %s", ('%' + keyword + '%',))
    # 获取查询结果
    result1 = cursor.fetchall()

    cursor.execute("SELECT * FROM PreApprovalPublicity WHERE title LIKE %s", ('%' + keyword + '%',))
    result2 = cursor.fetchall()

    results = result1 + result2
    # 返回搜索结果页面
    return render_template('search_results.html', results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=80)
