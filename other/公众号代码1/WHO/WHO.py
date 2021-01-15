#参考来源：https://blog.csdn.net/qq_44315987/article/details/104925840
import urllib.request, requests, json, time
from bs4 import BeautifulSoup
import pandas as pd

def getPdfs():
    url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports"
    strhtml=requests.get(url)
    soup=BeautifulSoup(strhtml.text,'lxml')
    datas = soup.select('div#PageContent_C006_Col01 > div.sf-content-block.content-block > div a')
    for data in datas:
        downloadUrl = 'https://www.who.int' + data['href'] #下载路径
        try:
            r = requests.get(downloadUrl)
            pdf = r.content  # 响应的二进制文件
            if (data.get_text()):
                with open(data.get_text() + ".pdf", 'wb') as f:  # 二进制写入
                    f.write(pdf)
                    print(data.get_text() + ".pdf" + "下载成功")
        except requests.exceptions.ConnectionError:
            r.status_code = "Connection refused"

res = pd.DataFrame()
def openUrl(url):
    heads = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    req = urllib.request.Request(url, headers=heads)
    response = urllib.request.urlopen(url)
    html = response.read()
    return html.decode('utf-8')

def conserve(html, name):
    global res
    time, confirm = [], []
    temp = pd.DataFrame(columns=['time', name])
    if name == 'America':
        for i in html['features']:
            time.append(i['attributes']['DateOfDataEntry'])
            confirm.append(i['attributes']['cum_conf'])
        temp['time'] = time
        temp[name] = confirm
        temp = temp.set_index('time')
        res = pd.concat([res, temp], axis=1)
    else:
        for i in html['features']:
            time.append(i['attributes']['DateOfDataEntry'])
            confirm.append(i['attributes']['NewCase'])
        temp['time'] = time
        temp[name] = confirm
        temp = temp.set_index('time')
        res = pd.concat([res, temp], axis=1)


def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y%m%d", timeArray)
    return otherStyleTime


def getDatas():
    global res
    for name in ['China', 'Italy', 'Spain', 'France', 'Germany', 'Switzerland', 'Netherlands', 'Norway', 'Belgium', 'Sweden', 'Australia', 'Brazil', 'Egypt']:

        url = 'https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Historic_adm0_v3/FeatureServer/0/query?f=json&where=ADM0_NAME%3D%27' + name + '%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=OBJECTID%2CNewCase%2CDateOfDataEntry&orderByFields=DateOfDataEntry%20asc&resultOffset=0&resultRecordCount=2000&cacheHint=true'
        html = json.loads(openUrl(url))
        conserve(html, name)
        print(name+"疫情数据下载成功")

    #America 单独拿出来
    name = 'America'
    url = 'https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Historic_adm0_v3/FeatureServer/0/query?f=json&where=ADM0_NAME%3D%27United%20States%20of%20America%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=OBJECTID%2Ccum_conf%2CDateOfDataEntry&orderByFields=DateOfDataEntry%20asc&resultOffset=0&resultRecordCount=2000&cacheHint=true'
    html = json.loads(openUrl(url))
    conserve(html, name)
    print(name + "疫情数据下载成功")
    res['Datetime'] = pd.date_range(start='20200111', end=timeStamp(res.index.get_level_values(0).values[-1]))
    res.to_csv('Datas.csv', encoding='utf_8_sig')

#getPdfs()
getDatas()
