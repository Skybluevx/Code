"""
    正则表达式的学习
"""
import requests
import re


def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Referer": "https://www.ygdy8.com/html/gndy/dyzz/index.html"
    }
    response = requests.get(url, headers=headers)
    element = response.content.decode()
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', element, re.S)
    dynasties = re.findall(r'<p class="source"><a.*?>(.*?)</a>', element, re.DOTALL)
    authors = re.findall(r'<p class="source">.+?<a.*?>(.*?)</a>', element, re.DOTALL)
    texts = re.findall(r'<div class="contson".*?>(.*?)</div>', element, re.DOTALL)
    contents = []
    for content in texts:
        x = re.sub("<.*?>", "", content)
        contents.append(x.strip())

    poems = []
    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        poem = {
            "title": title,
            "dynasty": dynasty,
            "author": author,
            "content": content
        }
        poems.append(poem)

    for poem in poems:
        print(poem)


def main():
    url_based = "https://www.gushiwen.org/default_{}.aspx"
    for x in range(1, 10):
        url = url_based.format(x)
        parse_page(url)


if __name__ == '__main__':
    main()
