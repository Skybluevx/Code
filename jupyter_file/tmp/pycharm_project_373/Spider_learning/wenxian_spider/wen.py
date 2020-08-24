"""
    作者：硕硕
    预期目标：实现对知网、知乎、CSDN、博客园的关键词搜索，爬取相关文章
    2020年4月20日之前：完成了对 CSDN 的爬取，初步尝试了对知网、知乎的爬取，但是失败，
                    目前还没有找到解决办法。而博客园目前已经快解决了，不过准确性还不高。
"""
import time
import requests
from lxml import etree
import csv
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from PIL import Image
from io import BytesIO
import cv2 as cv


# 浏览器驱动器绝对路径
CHORME_DRIVER_PATH = "./chromedriver.exe"

# 浏览器伪装
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"


class CsdnSpider(object):

    def __init__(self):
        self.base_url = r"https://so.csdn.net/so/search/s.do?p=1&q={}&t=blog&o=&s=&l=&f=&viparticle="
        self.base_url2 = "https://so.csdn.net/so/search/s.do"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
        self.referer = "https://www.csdn.net/"
        self.num = 0

        self.title = "title"
        self.key = "key"
        self.author = "author"
        self.people = "people"
        self.release_time = "time"
        self.url = "url"
        self.introduction = "introduction"

        self.header = [self.title, self.key, self.author, self.people,
                       self.release_time, self.url, self.introduction]

        self.file_name = "CSDN博客_"
        self.key_word = ""

    def get_context_data(self, url):
        response = requests.get(url, headers=self.headers, timeout=5)
        time.sleep(1.0)
        text = response.content.decode()
        # print(url)
        code = response.status_code
        # print("网页状态码为：{}".format(code))
        return text

    def get_infos(self, content):
        wz_list = []
        html = etree.HTML(content)
        info_list = html.xpath(
            '//div[@class="search-list-con"]//dl[@class="search-list J_search"]')

        for info in info_list:
            info_dict = {}

            # 文章标题（已经尽可能多的做好兼容性了）
            title = info.xpath('.//div[@class="limit_width"]/a/text()')
            key_word = info.xpath('.//div[@class="limit_width"]/a/em/text()')
            # 获取文章关键字
            try:
                info_dict[self.key] = key_word[0]
            except IndexError:
                info_dict[self.key] = ""

            try:
                if len(title) == 0:
                    info_dict[self.title] = key_word[0]
                elif len(title) == 1:
                    if title[0].endswith("CSDN博客"):
                        continue
                    elif len(key_word) == 0:
                        info_dict[self.title] = title[0]
                    else:
                        info_dict[self.title] = key_word[0] + " " + title[0]
                elif len(title) == 2:
                    if title[1].endswith("CSDN博客"):
                        if len(key_word) == 0:
                            info_dict[self.title] = title[0]
                        else:
                            info_dict[self.title] = title[0] + key_word[0]
                    else:
                        if len(key_word) == 0:
                            info_dict[self.title] = title[0] + title[1]
                        else:
                            info_dict[self.title] = title[0] + \
                                key_word[0] + title[1]
                elif len(title) == 3:
                    if title[2].endswith("CSDN博客"):
                        if len(key_word) == 1:
                            info_dict[self.title] = title[0] + \
                                key_word[0] + title[1]
                        elif len(key_word) == 2:
                            info_dict[self.title] = title[0] + \
                                key_word[0] + title[1] + key_word[1]
                elif len(title) == 4:
                    if title[3].endswith("CSDN博客"):
                        if len(key_word) == 2:
                            info_dict[self.title] = title[0] + key_word[0]\
                                + title[1] + key_word[1] + title[2]
                        elif len(key_word) == 3:
                            info_dict[self.title] = title[0] + key_word[0] + \
                                title[1] + key_word[1] + title[2] + key_word[2]
                else:
                    info_dict[self.title] = "标题太长，无法显示！"
            except IndexError:
                info_dict[self.title] = "标题获取出错！"

            # author_time
            author_time = info.xpath('.//dd[@class="author-time"]')[0]

            # 文章作者
            info_dict[self.author] = author_time.xpath('./a/text()')[0]

            # 文章浏览量
            info_dict[self.people] = author_time.xpath(
                './span[@class="mr16"]/text()')[0]

            # 文章发布时间
            info_dict[self.release_time] = author_time.xpath(
                './span[@class="date"]/text()')[0]

            # 文章链接
            info_dict[self.url] = info.xpath(
                './/div[@class="limit_width"]/a/@href')[0]

            # 文章简介
            info_dict[self.introduction] = info.xpath(
                './/dd[@class="search-detail"]/text()')[0]

            wz_list.append(info_dict)
            self.num += 1
            print("已成功获取第{}篇CSDN文章信息！标题：{}".format(
                self.num, info_dict[self.title]))

        # print(wz_list)
        return wz_list

    def save_to_csv(self, file_name, wz_list):
        with open(file_name, mode="a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, self.header)
            writer.writerows(wz_list)

    def __creat_file(self, file_name):
        with open(file_name, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, self.header)
            writer.writeheader()

    def get_the_next_url(self, content):
        html = etree.HTML(content)
        try:
            url = html.xpath(
                '//span[@class="page-nav"]/'
                'a[@class="btn btn-xs btn-default btn-next checklogin"]/@href')[0]
            next_url = self.base_url2 + url
            return next_url
        except IndexError:
            print("已经没有下一页啦~~")
            return False

    def run(self, key_word):

        # 设置默认关键字
        self.key_word = key_word
        if self.key_word == "":
            self.key_word = "jupyter"

        # 设置文件名
        self.file_name = self.file_name + self.key_word + ".csv"
        self.__creat_file(self.file_name)
        url = self.base_url.format(self.key_word)
        while url:
            self.headers["Referer"] = self.referer
            content_data = self.get_context_data(url)
            wz_list = self.get_infos(content_data)
            self.save_to_csv(self.file_name, wz_list)
            url = self.get_the_next_url(content_data)
            self.referer = url
        print("CSDN网站已爬取完毕，保存文件名为：{}".format(self.file_name))


class ZhiHuSpider(object):

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
            "537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Referer": "https://www.zhihu.com/signin?next=%2F",
            "content-type": "application/x-www-form-urlencoded",
            "x-zse-83": "3_2.0",
            "x-xsrftoken": "8Itbemsh23h5BnfV3pfU1qSGdpr5Zqt3"}
        self.referer = "https://www.zhihu.com/signin?next=%2F"

        self.account = "17134025325"
        self.password = "369852147l"

        self.zhihu_url = "https://www.zhihu.com"
        self.login_url = "https://www.zhihu.com/api/v3/oauth/sign_in"
        self.chrome_driver_path = CHORME_DRIVER_PATH

    def get_cookie(self):

        # 创建浏览器驱动
        driver = webdriver.Chrome(executable_path=self.chrome_driver_path)

        # 设置参数让网站无法识别浏览器为程序驱动浏览器
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

        # 将浏览器设置为最大化
        driver.maximize_window()

        # 打开浏览器，并跳转指定网页
        driver.get(self.zhihu_url)

        time.sleep(200)
        driver.close()

    def run(self):
        self.get_cookie()


class BlogSpider(object):

    def __init__(self):
        self.base_url = "https://zzk.cnblogs.com/s?t=b&w={}"

        self.driver = webdriver.Chrome(executable_path=CHORME_DRIVER_PATH)
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """
        })

        self.location = {}
        self.size = {'width': 260, 'height': 160}
        self.wait = WebDriverWait(self.driver, 20)
        self.bg_img_path = "./bg_img.png"
        self.slice_img_path = "./slice_img.png"

    def get_content(self, url):

        # 创建浏览器启动器，设置参数
        self.driver.maximize_window()

        self.driver.get(url)

        time.sleep(0.5)
        # 滑块验证
        self.yanzheng()
        time.sleep(200)
        self.driver.close()

    def yanzheng(self):
        self.get_img()
        value_1, value_2 = self.img_match_path(self.bg_img_path, self.slice_img_path)
        print("最差匹配坐标：{}，最佳匹配坐标：{}".format(value_1, value_2))

        # 获取滑动按钮
        button = self.wait.until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "geetest_slider_button"))
        )
        action = ActionChains(driver=self.driver)
        # try:
        action.click_and_hold(button).perform()
        # except StaleElementReferenceException as e:
        #     print(e)

        action.reset_actions()

        forward_tracks, back_tracks = self.generate_tracks(value_2)

        for x in forward_tracks:
            # 前进移动滑块
            action.move_by_offset(x, 0)
            print(x)
        action.perform()
        action.reset_actions()

        print("#" * 50)

        for x in back_tracks:
            # 后退移动滑块
            action.move_by_offset(x, 0).perform()
            print(x)
        action.perform()
        action.reset_actions()

        action.release().perform()

    def generate_tracks(self, distance):
        distance += 20
        v = 0
        t = 0.2
        forward_tracks = []
        current = 0

        # 减速阀值
        mid = distance * 3 / 5
        while current < distance:
            if current < mid:
                # 速度为+2
                a = 2
            else:
                # 速度-3
                a = -3

            s = v * t + 0.5 * a * (t ** 2)
            v = v + a * t
            current += s
            forward_tracks.append(round(s))

        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1, -1]
        return forward_tracks, back_tracks

    def img_match_path(self, bg_img_path, slice_img_path):
        bg_img = cv.imread(bg_img_path)
        bg_img_gray = cv.cvtColor(bg_img, cv.COLOR_BGR2GRAY)
        slice_img_gray = cv.imread(slice_img_path, 0)
        res = cv.matchTemplate(bg_img_gray, slice_img_gray, cv.TM_CCOEFF_NORMED)
        value = cv.minMaxLoc(res)
        value_1 = value[2:][0][0]
        value_2 = value[2:][1][0]
        return value_1, value_2

    def get_screenshot(self, img_type):
        self.driver.get_screenshot_as_file("./screenshot.png")
        screenshot = Image.open("./screenshot.png")
        if img_type == "bg":
            self.get_bg_img(screenshot)
        elif img_type == "slice":
            self.get_slice_img(screenshot)

    def get_bg_img(self, scrennshot):
        left, top, right, bottom = (
            self.location['x'] - 10, self.location['y'] + 10, self.location['x'] + self.size['width'] - 3,
            self.location['y'] + self.size['height'] - 10
        )
        bg_img = scrennshot.crop((left, top, right, bottom))
        bg_img.save(self.bg_img_path)

    def get_slice_img(self, screenshot):
        left, top, right, bottom = (
            self.location['x'], self.location['y'], self.location['x'] + 70,
            self.location['y'] + self.size["height"]
        )
        print(
            "验证码位置：left：{}，top：{}，right：{}，bottom：{}".format(
                left, top, right, bottom))
        slice_img = screenshot.crop((left, top, right, bottom))
        self.deal_with_slice_img(slice_img)

    def deal_with_slice_img(self, slice_img):
        img = slice_img
        pixel = 220
        width, height = img.size
        height_num = []
        width_num = []
        for i in range(height):
            for m in range(int(width / 3 * 2)):
                a, z, x, c = img.getpixel((m, i))
                if x < pixel:
                    # print(i)
                    height_num.append(i)
                    break
        for i in range(width):
            for o in range(height):
                a, z, x, c = img.getpixel((i, o))
                if x < pixel:
                    # print(i)
                    width_num.append(i)
                    break
        # print(height_num, width_num)
        height_up_line = height_num[0] + 5
        height_down_line = height_num[-1] - 5
        width_left_line = width_num[0] + 5
        width_right_line = width_num[-1] - 5
        result = img.crop(
            (width_left_line,
             height_up_line,
             width_right_line,
             height_down_line))
        result.save(self.slice_img_path)

    def get_img(self):
        ele = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.TAG_NAME, "canvas")))
        # ele = self.driver.find_elements_by_tag_name("canvas")
        print(ele)
        self.location = ele[0].location

        # 移除带缺口的图片，至显示滑块图片
        self.setAttribute(ele[0], "style", "display: none;")
        self.get_screenshot("slice")
        time.sleep(0.3)

        # 移除滑块图片，显示完整背景图片
        self.setAttribute(ele[1], "style", "display: none;")
        time.sleep(0.3)
        self.setAttribute(ele[2], "style", "display: 1")
        time.sleep(0.3)
        self.get_screenshot("bg")
        time.sleep(0.3)

        # 隐藏完整背景图片，显示滑块，显示代缺口的图片
        self.setAttribute(ele[2], "style", "display: none;")
        time.sleep(0.1)
        self.setAttribute(ele[1], "style", "display: 1")
        time.sleep(0.1)
        self.setAttribute(ele[0], "style", "display")

    def setAttribute(self, elementObj, attributeName, value):
        # 封装设置页面对象的属性值的方法
        # 调用JavaScript代码修改页面元素的属性值，arguments[0]－［2］分别会用后面的
        # element、attributeName和value参数值进行替换，并执行该JavaScript代码
        self.driver.execute_script(
            "arguments[0].setAttribute (arguments[1],arguments[2])",
            elementObj,
            attributeName,
            value)

    def removeAttribute(self, elementObj, attributeName):
        # 封装删除页面元素属性的方法
        # 调用JavaScript代码删除页面元素的指定的属性，arguments[0]－［1］分别会用后面的
        # element、attributeName参数值进行替换，并执行该JavaScript代码
        self.driver.execute_script(
            "arguments[0].removeAttribute(arguments[1])",
            elementObj,
            attributeName)

    def run(self, key_word):
        self.get_content(self.base_url.format(key_word))


class ZhiWangSpider(object):

    def __init__(self):
        self.start_url = "https://cnki.net/"
        self.start_url2 = "https://kns.cnki.net/kns/brief/default_result.aspx"
        self.headers = {
            "User-Agent": USER_AGENT
        }
        self.data = {
            'pagename': 'ASP.brief_default_result_aspx',
            'isinEn': '1',
            'dbPrefix': 'SCDB',
            'dbCatalog': '中国学术文献网络出版总库',
            'ConfigFile': 'SCDBINDEX.xml',
            'research': 'off',
            't': '1586956674925',
            'keyValue': '',
            'S': '1',
            'sorttype': '',
            'DisplayMode': 'custommode'
        }

    def get_content(self, url, key_word):
        options = Options()
        driver = webdriver.Chrome(CHORME_DRIVER_PATH, chrome_options=options)
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)
        driver.get(url)

        # 找到搜索框并输入关键词
        # search_input = driver.find_element_by_class_name("search-input")
        search_input = wait.until(
            expected_conditions.presence_of_element_located(
                (By.NAME, "txt_1_value1")))
        # print(search_input)
        # print(key_word)
        search_input.send_keys(key_word)

        time.sleep(1)

        # 找到搜索按钮并点击
        # button = driver.find_element_by_class_name("search-btn")
        button = wait.until(
            expected_conditions.presence_of_element_located(
                (By.ID, "btnSearch")))
        # print(button)
        button.click()
        print(driver.get_cookies())
        url1 = "https://kns.cnki.net/kns/brief/brief.aspx?pagename=" \
               "ASP.brief_default_result_aspx&isinEn=1&dbPrefix=SCDB&" \
               "dbCatalog=中国学术文献网络出版总库&ConfigFile=SCDBINDEX.xml&research=off&t={time}" \
               "&keyValue={key_word}&S=1&sorttype=&DisplayMode=custommode".format(time=self.now_time(),
                                                                                  key_word=key_word)
        response = requests.post(
            url1,
            headers=self.headers,
            cookies=driver.get_cookies())
        print(response.content.decode())
        time.sleep(200)
        driver.close()

    def now_time(self):
        ti = time.time()
        t = int(ti * 1000)
        return t

    def get_content2(self, url, key_word):
        session = requests.session()
        self.data["keyValue"] = key_word
        self.data["t"] = str(self.now_time())
        print(self.now_time())
        response = session.post(url, data=self.data, headers=self.headers)
        content = response.content.decode()
        # print(content)

        url1 = "https://kns.cnki.net/kns/brief/brief.aspx?pagename=" \
            "ASP.brief_default_result_aspx&isinEn=1&dbPrefix=SCDB&" \
            "dbCatalog=中国学术文献网络出版总库&ConfigFile=SCDBINDEX.xml&research=off&t={time}" \
            "&keyValue={key_word}&S=1&sorttype=&DisplayMode=custommode".format(time=self.now_time(), key_word=key_word)
        response = session.get(url1, headers=self.headers)
        # response2 = requests.get(url=url1, headers=self.headers, cookies=response.cookies)
        print(response.content.decode())
        return content

    def get_infos_list(self, content):
        html = etree.HTML(content)
        text = html.xpath(
            '//div[@class="GridContent"]//div[@class="GridRightColumn"]//a/text()')
        print(text)

    def run(self, key_word):
        self.get_content(self.start_url2, key_word)


def main():
    key = input("请输入搜索关键词：")
    if key == "":
        key = "jupyter"
    start = time.time()
    # spider = CsdnSpider()
    # spider.run(key_word=key)
    # zhihu_spider = ZhiHuSpider()
    # zhihu_spider.run()
    blog_spider = BlogSpider()
    blog_spider.run(key)
    # zhiwang_spider = ZhiWangSpider()
    # zhiwang_spider.run(key_word=key)
    print("总耗时：{}".format(time.time() - start))


if __name__ == '__main__':
    main()
