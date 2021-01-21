import json
import requests


url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1574086511372"
headers = {"User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
           "Referer": "https://m.douban.com/tv/american"
           }

response = requests.get(url, headers=headers, timeout=5)
json_str = response.content.decode()
ret1 = json.loads(json_str)
# print(ret1)

# with open("douban.txt", "w", encoding="utf-8") as f:
#     # ensure_ascii参数表示保存的文件不再以ascii码保存，是中文就保存中文
#     # indent参数能让下一行在上一行的基础上空指定格数
#     f.write(json.dumps(ret1, ensure_ascii=False, indent=2))

print(ret1["subject_collection_items"][0])
