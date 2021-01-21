import requests
from bs4 import BeautifulSoup

a = [[0 for col in range(3)] for row in range(318)]


def gethtmltext(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    try:
        r = requests.get(url, timeout=30, headers=headers)
        # r.raise_for_status()
        # result=r.text.encode("latin1").decode("gbk")
        r.encoding = 'utf-8'
        # print(r.text)
        return r.text
    except:
        print('错误')
        return ""


def fillweather(soup):
    j = i = 0
    city_name_list = soup.find_all(class_='td td-2nd')
    city_num_list = soup.find_all(class_='td td-4rd')
    while i < len(city_name_list):
        city_name = city_name_list[i].get_text()
        city_num = city_num_list[j].get_text()
        city_info = city_num_list[j + 1].get_text()
        a[i][0] = city_name
        a[i][1] = city_num
        a[i][2] = city_info
        i = i + 1
        j = j + 2


def printweather():
    print('排名', '城市', '空气质量指数', '质量状况')
    for i in range(317):
        print(i + 1, a[i])


def main():
    url = 'http://www.tianqi.com/air'
    html = gethtmltext(url)
    if (html != ''):
        soup = BeautifulSoup(html, 'html.parser')
        fillweather(soup)
        printweather()


if __name__ == '__main__':
    main()
