#/usr/bin/ python3
# -*- coding:utf-8 -*-

#获取猫眼电影排行榜的前一百个电影
import requests
from requests.exceptions import RequestException
from selenium import webdriver
from lxml import etree
from multiprocessing import Pool

def get_one_page(url):
    browser = webdriver.Chrome()
    try:
        browser.get(url)
        return browser.page_source
    finally:
        browser.close()

# 提示禁止访问
# def getHTMLText(url):
#     try:
#         response = requests.get(url='http://maoyan.com/board/4')
#         print(response.raise_for_status())
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         return None


def parseOnePage(html):
    res = etree.HTML(html)
    ranking = res.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/i/text()')
    # print(ranking)
    name = res.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a/text()')
    actors = res.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[2]/text()')
    time = res.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[3]/text()')
    imgurl = res.xpath('//*[@class="board-img"]')
    img = res.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/a/img[2]/@src')
    print(img)

    #方法一:构造[{}],循环,自定义字典的k ,把v循环进去
    # a = []
    # for i in range(len(ranking)):
    #     b = {}
    #     b['ranking'] = ranking[i]
    #     b['name'] = name[i]
    #     b['actors'] = actors[i].strip()[3:]
    #     b['time'] = time[i].strip()[5:]
    #     b['imgurl'] = imgurl[i].attrib['data-src']
    #     a.append(b)
    # print(a)




    #方法二:使用zip(),合并多个列表,并且配合生成器输出结果
    lst = zip(ranking,name,actors,time,imgurl)
    # print(lst)
    lists = list(lst)
    print(lists)
    for i in lists:
        yield {
            "排名":i[0],
            "电影名称":i[1],
            "主演":i[2].strip()[3:],
            "上映时间":i[3].strip()[5:],
            "图片链接":i[4].attrib['data-src']
        }


    #方法三:zip()繁琐使用
    # lst = zip(ranking,name,actors,time,imgurl)
    # # print(lst)
    # lists = list(lst)
    # print(lists)
    # c = []
    # for i in lists:
    #     d = {}
    #     d['ranking'] = list(i)[0]
    #     d['name'] = list(i)[1]
    #     d['actors'] = list(i)[2].strip()[3:]
    #     d['time'] = list(i)[3].strip()[5:]
    #     d['imgurl'] = list(i)[4].attrib['data-src']
    #     c.append(d)
    # # print(c)


def write_to_file(content):#将爬取到的电影信息保存到本地文件夹
   with open('m.txt', 'a', encoding='utf-8')as f:
       f.write( str(content) + '\n')
       f.close()




def main(offeset):
    url = 'http://maoyan.com/board/4?' + str(offeset)
    # html = getHTMLText(url)
    html = get_one_page(url)
    parseOnePage(html)
    for item in parseOnePage(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)

        pool = Pool()
        pool.map(main,[i*10 for i in range(10)])


