import json

import requests


KEY = '1f136301d56d4df482527d838f862573'


class AiChat(object):

    def __init__(self):
        self.menu_dict = {
            "智能对话": [self.tulin],
        }

    @staticmethod
    def tulin():
        info = 'w'
        for i in range(10):
            if info == '[退出]':
                break
            print("小安:如果没有ID和密码,请在ID输入“YH-ZJ”,请在密码输入“1001”(登录这个ID需要一个图灵机器人)")
            print("小安:请输入ID")
            ID = input("我:")
            print("小安:请输入密码")
            MM = input("我:")
            if ID == 'CYG-GLY' and MM == '12131':
                print("小安:现在你能和我对话了哟,不过记得先连网,如过不想和我对话了可以输入“[退出]”")
                try:
                    while True:
                        info = input('我:')  # 输入对话信息
                        if info == '[退出]':
                            print("小安:退出")
                            break
                        url = 'http://www.tuling123.com/openapi/api?key=' + KEY + '&info=' + info  # 拼接 url
                        res = requests.get(url)  # 得到数据
                        res.encoding = 'utf-8'  # 防止中文乱码
                        data = json.loads(res.text)  # 将得到的 json 格式的信息转换为 Python 的字典格式
                        print('小安:' + data['text'])  # 输出结果
                except:
                    print("对话失败,请确认网络是否连接")
            elif ID == 'YH-KK' and MM == '0100':
                key_TY = 'b7e054da696f40d8b026a40435c0a7e4'
                print("小安:现在你能和我对话了哟,不过记得先连网,如过不想和我对话了可以输入“[退出]”")
                try:
                    while True:
                        info = input('我:')  # 输入对话信息
                        if info == '[退出]':
                            print("小安:退出")
                            break
                        url = 'http://www.tuling123.com/openapi/api?key=' + key_TY + '&info=' + info  # 拼接 url
                        res = requests.get(url)  # 得到数据
                        res.encoding = 'utf-8'  # 防止中文乱码
                        data = json.loads(res.text)  # 将得到的 json 格式的信息转换为 Python 的字典格式
                        print('小安:' + data['text'])  # 输出结果
                except:
                    print("对话失败,请确认网络是否连接")
            elif ID == 'YH-ZJ' and MM == '1001':
                print("小安:请输入图灵aip")
                key_YH = input("我:")
                print("小安:现在你能和我对话了哟,不过记得先连网,如过不想和我对话了可以输入“[退出]”")
                try:
                    while True:
                        info = input('我:')  # 输入对话信息
                        if info == '[退出]':
                            print("小安:退出")
                            break
                        url = 'http://www.tuling123.com/openapi/api?key=' + key_YH + '&info=' + info  # 拼接 url
                        res = requests.get(url)  # 得到数据
                        res.encoding = 'utf-8'  # 防止中文乱码
                        data = json.loads(res.text)  # 将得到的 json 格式的信息转换为 Python 的字典格式
                        print('小安:' + data['text'])  # 输出结果
                except:
                    print("对话失败,请确认网络是否连接")

            else:
                print("小安:密码或ID错误")
                CW = 9 - i
                print("小安:你还有{}次机会".format(CW))
                if CW == 0:
                    print("小安:退出智能对话")
                    break
