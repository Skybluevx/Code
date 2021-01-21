import requests
import json
import proxypool.proxy as ppool
from lxml import etree
from retrying import retry  # 通过装饰器来重复执行装饰后的代码

# url = "https://www.baidu.com"
url = "https://careers.tencent.com/tencentcareer/api/post/Query?countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=2&pageSize=10&language=zh-cn&area=cn"
url2 = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1574607724728&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=3&pageSize=10&language=zh-cn&area=cn"
url3 = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
}
dete = ""


# get 请求
# response = requests.get(url3, headers=headers)
# post 请求
# response = requests.post(url, dete=date)

# 三种解码方式
# url_str = response.content.decode()
# url_str = response.content.decode("gbk")
# url_str = response.content.decode()

# json_str = json.dumps(url_str, ensure_ascii=False)
# dict1 = json.loads(url_str)["Data"]["Posts"]
# print(dict1)

# # 在函数报错的情况下，把函数最多执行三次
# @retry(stpo_max_attempt_num=3)
# def pares():
#     pass
# requests.get(url, headers=headers, timeout=3)
ip = ppool.Spider()
ip_list = ip.get_ip(num=20)
print(ip_list)