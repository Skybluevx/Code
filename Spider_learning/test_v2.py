import requests
import json


# url = "https://fanyi.baidu.com/basetrans"
url = "https://fanyi.baidu.com/sug"
headers = {"User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"}
# data = {"query": "你好，世界",
#         "from": "zh",
#         "to": "en",
#         "token": "81afd651eba91fcee630aa925bc9834b",
#         "sign": "933122.712243"}
data = {
    "kw": "世界"
}
response = requests.post(url, headers=headers, data=data, timeout=3)
html_str = response.content.decode()

# json.loads函数把json类型的字符串转换为python类型
text_dict = json.loads(html_str)
# json.dumps函数可把python类型转换为json类型

text = text_dict["data"][0]["v"].split(";")[0].split(" ")[-1]

print(text)
