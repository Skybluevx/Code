import requests
import parsel#
import re

base_url='http://www.jianpuw.com/'

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
prox={'HTTP': '117.88.5.118:3000'}
response=requests.get(base_url,headers=headers,proxies=prox)
response.encoding=response.apparent_encoding
html=response.text
#print(html)
parse=parsel.Selector(html)#转换后的数据类型。返回Selector对象
#3.2数据提取
href_list=parse.xpath('//html/body/div/ul/li/a').extract()
#print(href_list)

base_url1='http://www.jianpuw.com/htm/kz/'
base_url0='http://www.jianpuw.com/'

for href in href_list:
    href1=re.findall('<a href="../../htm/.*?/(.*?)">(.*?)</a>',href)
    #print(href1)
    if len(href1)>0:
        # print(href1)
        url1=href1[0][0]
        name1=href1[0][1]
        # print(url1)
        # print(name1)
        url2=base_url1+url1
        # print(url2)
        response1 = requests.get(url2, headers=headers,proxies=prox)
        response1.encoding = response1.apparent_encoding
        img1=response1.text
        # print(img1)
        tu_name=re.findall('<img src="../../(.*?)" title="(.*?)" />',img1)
   
        # print(tu_name[0])
        img_url=base_url0+tu_name[0][0]
        # img_name=tu_name[0][1]
        print(img_url)
        # print(img_name)
        # ji=input("暂停")
        img_name=img_url.split('/')[-1]

        tu=requests.get(img_url, headers=headers,proxies=prox).content

        with open('img\\'+img_name, 'wb') as f:
            f.write(tu)
    else:
        pass

