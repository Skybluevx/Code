import hashlib
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime


class Translation(object):

    def __init__(self):
        self.menu_dict = {
            "翻译": [self.translate]
        }

    @staticmethod
    def translate():
        try:
            while True:
                print("小安:请输入中文或英文(仅限英文和中文),输入“[退出]”退出")
                d = input('我:')
                if d == '[退出]':
                    print("小安:退出翻译")
                    break
                heads = {}
                heads['User-Agent'] = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'

                now = datetime.now()
                now = now.timestamp()

                a = re.match(r'(\d+)\.(\d+)', str(now))
                b = a.group(1) + a.group(2)
                f = b[:13]  # 时间戳前13位

                c = "rY0D^0'nM0}g5Mm1z%1G4"
                u = 'fanyideskweb'

                creatmd5 = u + d + f + c

                # 生成md5
                md5 = hashlib.md5()
                md5.update(creatmd5.encode('utf-8'))
                sign = md5.hexdigest()

                url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='

                data = {}
                data['i'] = d
                data['from'] = 'AUTO'
                data['to'] = 'AUTO'
                data['smartresult'] = 'dict'
                data['client'] = 'fanyideskweb'
                data['salt'] = f
                data['sign'] = sign
                data['doctype'] = 'json'
                data['version'] = '2.1'
                data['keyfrom'] = 'fanyi.web'
                data['action'] = 'FY_BY_CLICKBUTTION'
                data['typoResult'] = 'true'

                data = urllib.parse.urlencode(data).encode('utf-8')

                req = urllib.request.Request(
                    url=url, data=data, method='POST', headers=heads)
                # 想要使用动态追加头headers，必须使Request类实例化，对象有动态追加函数req.add_headers()的方法
                response = urllib.request.urlopen(req)

                translateResult = response.read().decode('utf-8')

                target = json.loads(translateResult)

                print(target['translateResult'][0][0]['tgt'])
        except BaseException:
            print("小安:翻译失败，请检查网络是否连接")
            print("小安:退出翻译")
