import requests
from lxml import etree


url = "https://movie.douban.com/chart"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

response = requests.get(url, headers=headers)
html_str = response.content.decode()

html = etree.HTML(html_str)
url_list = html.xpath("//div[@class='pl2']/a//text()")
for i in url_list:
    a = i.replace("/", "")
    print(a.strip())
