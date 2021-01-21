# *-* coding:utf-8 *-*
from flask import Flask, render_template

# 创建 Flask 应用程序
app = Flask(__name__)

# 定义路由(通过装饰器实现的)及视图函数
# 路由默认只有GET，如果需要增加，需要自行指定
@app.route("/")
def index():
    url_str = "www.baid.com"
    return render_template('index.html', url_str=url_str)
    # return "halou"


if __name__ == '__main__':
    app.run(debug=True)
