import json
import requests
from requests.exceptions import RequestException
import re
from selenium import webdriver
from multiprocessing import Pool

def get_one_page(url):
    browser = webdriver.Chrome()
    try:
        browser.get(url)
        return browser.page_source
    finally:
        browser.close()


# def get_one_page(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                        +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                        +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'ranking':item[0],
            'image':item[1],
            'name':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5] + item[6]
        }


def write_to_file(content):#将爬取到的电影信息保存到本地文件夹
   with open('movie.txt', 'a', encoding='utf-8')as f:
       f.write(json.dumps(content,ensure_ascii=False) + '\n')
       f.close()


def main(offeset):
    url = 'http://maoyan.com/board/4?' + str(offeset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)

        pool = Pool()
        pool.map(main,[i*10 for i in range(10)])