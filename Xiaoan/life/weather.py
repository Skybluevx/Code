import json
import re

import requests


class Weather(object):

    def __init__(self):
        self.menu_dict = {
            "天气查询": [self.weather_inquire],
        }

    @staticmethod
    def weather_inquire():
        while True:
            try:
                print("小安:请输入查询的城市(输入“退出”退出):")
                str1 = input("我:")
                if str1 == '退出':
                    print("小安:退出天气查询")
                    break
                url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + str1
                response = requests.get(url)
                wearher_json = json.loads(response.text)
                a = wearher_json['data']
                print("当前位置：" + a['city'])
                print("温馨提示：" + a['ganmao'])
                print("当前温度：" + a['wendu'] + '℃')
                print("昨天：" + a['yesterday']['date'])
                print("风力：" + a['yesterday']['fl'][9:[m.start()
                                                      for m in re.finditer(']', a['yesterday']['fl'])][0]])
                print("风向：" + a['yesterday']['fx'])
                print(a['yesterday']['high'])
                print(a['yesterday']['low'])
                print("天气：" + a['yesterday']['type'])
                print("--------------------------------")
                for i in range(0, 4):
                    print("时间：" + a["forecast"][i]['date'])
                    print('风力: ' + a["forecast"][i]['fengli'][9:[m.start()
                                                                 for m in re.finditer(']', a['yesterday']['fl'])][0]])
                    print('风向：' + a["forecast"][i]['fengxiang'])
                    print(a["forecast"][i]['high'])
                    print(a["forecast"][i]['low'])
                    print("天气：" + a["forecast"][i]['type'])
                    print("--------------------------------")
            except BaseException:
                print("小安:天气查询失败,请检查网络是否连接,或者请查看是否输入错误")
