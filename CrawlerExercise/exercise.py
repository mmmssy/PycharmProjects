# ~/usr/bin python3
# -*- coding:utf-8 -*-

# import requests
# import os
# url = "https://awsbj0-cdn.fds-ssl.api.xiaomi.com/20160324-01-huami-homepage/uploads/banners/5a375e11dab5c.jpg"
# root = "/home/maosiyi/图片/"
# path = root + url.split('/')[-1]
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             f.close()
#             print("文件保存成功")
#     else:
#         print("文件已存在")
# except:
#     print("爬取失败")

# import requests
# keyword = "python"
# try:
#     kv = {'wd' : keyword}
#     r = requests.get('https://www.baidu.com/s?wd=', params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(len(r.text))
# except:
#     print("爬取失败")

# import requests
# try:
#     kv = {'User-Agent' : 'Mozilla/5.0'}
#     r = requests.get('https://www.baidu.com/', headers = kv)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print("爬取失败")
#
# import requests
# from bs4 import BeautifulSoup
# import bs4
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout = 30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "爬取失败"
#
# def fillUnivList(ulist, html):
#     soup = BeautifulSoup(html, "html.parser")
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             ulist.append([tds[0].string, tds[1].string, tds[2].string])
#
# def printUnivList(ulist, num):
#     tpls = "{0:^10}\t{1:{3}^10}\t{2:^10}"
#     print(tpls.format("排名", "学校名称", "总分", chr(12288)))
#     for i in range(num):
#         u = ulist[i]
#         print(tpls.format(u[0], u[1], u[2], chr(12288)))
#
# def main():
#     uinfo = []
#     url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
#     html = getHTMLText(url)
#     fillUnivList(uinfo, html)
#     print(uinfo, 20)
# main()

# import requests
# from bs4 import BeautifulSoup
# import bs4
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout = 30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "爬取失败"
#
# def fillUnivList(ulist, html):
#     soup = BeautifulSoup(html, "html.parser")
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             ulist.append([tds[0].string, tds[1].string, tds[3].string])
#
# def printUnivList(ulist, num):
#     tpls = "{0:^10}\t{1:{3}^10}\t{2:^10}"
#     print(tpls.format("排名", "学校名称", "总分", chr(12288)))
#     for i in range(num):
#         u = ulist[i]
#         print(tpls.format(u[0], u[1], u[2], chr(12288)))
#
# def main():
#     uinfo = []
#     url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
#     html = getHTMLText(url)
#     fillUnivList(uinfo, html)
#     printUnivList(uinfo, 20)
# main()

# import requests
# import re
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout = 30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ""
#
#
# def parsePage(lst, html):
#     all_price = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
#     all_title = re.findall(r'\"raw_title\"\:\".*?\"', html)
#     for i in range(len(all_price)):
#         price = eval(all_price[i].split(':')[1])
#         title = eval(all_title[i].split(':')[1])
#         lst.append([price, title])
#
#
# def printInfo(lst):
#     tpls = "{:^4}\t{:^8}\t{:^16}"
#     print(tpls.format("序号", "价格", "商品名称"))
#     count = 0
#     for i in lst:
#         count = count + 1
#         print(tpls.format(count, i[0], i[1]))
#
#
# def main():
#     keyword = "书包"
#     start_url = 'https://s.taobao.com/search?q=' + keyword
#     depth = 3
#     goodslst = []
#     for i in range(depth):
#         try:
#             url = start_url + '&s=' + str(44 * i)
#             html = getHTMLText(url)
#             parsePage(goodslst, html)
#         except:
#             return ""
#     printInfo(goodslst)
# main()

import requests
import re
import traceback
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockList(lst,listurl):
    html = getHTMLText(listurl)
    soup = BeautifulSoup(html, 'html.parser')
    for i in soup.find_all('a'):
        try:
            href = i.attrs['href']
            lst.add(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs = {'class':'stock-bets'})

            name = stockInfo.find_all(attrs = {'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0], "股票代码":stock})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                print(fpath)
                f.write( str(infoDict) + '\n' )
        except:
            traceback.print_exc()
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'http://gupiao.baidu.com/stock/'
    list = set()
    path = '..\home\maosiyi\文档\a.txt'
    getStockList(list, stock_list_url)
    getStockInfo(list, stock_info_url, path)
main()



