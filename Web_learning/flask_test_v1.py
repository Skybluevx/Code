# *-* coding:utf-8 *-*
from flask import Flask, render_template

# 创建 Flask 应用程序
app = Flask(__name__)


# 定义路由(通过装饰器实现的)及视图函数
# 路由默认只有GET，如果需要增加，需要自行指定
@app.route("/", methods=["GET", "POST"])
def hello_world():
    return render_template("index.html")

# 使用同一个视图函数来显示显示不不同用户的订单信息
# <> 为动态参数名字
# @app.route("/orders/<int:order_list>")
# def get_order_id(order_list):
#     # 对路由动态参数进行优化，可在其前面加 int:/float:
#     # 需要在视图函数的（）内填入参数名，后面的代码才能够使用
#     return "order_id %s" % order_list


if __name__ == '__main__':
    app.run(debug=True)
