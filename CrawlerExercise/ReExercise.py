# ~/usr/bin python3
# -*- coding:utf-8 -*-

# #淘宝商品比价定向爬虫
# import requests
# import re
#
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout = 30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "爬取失败"
#
#
# def parsePage(ilt, html):
#     try:
#         all_price = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
#         all_name = re.findall(r'\"raw_title\"\:\".*?\"', html)
#         for i in range(len(all_name)):
#             price = eval(all_price[i].split(':')[1])
#             name = eval(all_name[i].split(':')[1])
#             ilt.append([price, name])
#     except:
#        return ""
#
#
# def printGoodsList(ilt):
#     tplt = "{:^4}\t{:^8}\t{:^16}"
#     print(tplt.format("序号", "价钱", "商品名称"))
#     count = 0
#     for g in ilt:
#         count = count + 1
#         print(tplt.format(count, g[0], g[1]))
#
# def main():
#     goods = '书包'
#     depth = 2    #爬取深度
#     start_url = 'https://s.taobao.com/search?q=' + goods
#     infoList = []
#     for i in range(depth):
#         try:
#             url = start_url + '&s=' + str(44*i)
#             html = getHTMLText(url)
#             parsePage(infoList, html)
#         except:
#             continue
#     printGoodsList(infoList)
# main()




# #股票数据定向爬虫
# import requests
# from bs4 import BeautifulSoup
# import re
# import traceback
#
# #获得url对应的页面
# def getHTMLText(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ""
#
# #获得股票的信息列表
# def getStockList(lst, stockURL):
#     html = getHTMLText(stockURL)
#     soup = BeautifulSoup(html, 'html.parser')
#     for i in soup.find_all('a'):
#         try:
#             href = i.attrs['href']
#             lst.add(re.findall(r"[s][hz]\d{6}", href)[0])
#         except:
#             continue
#
# #获得每一支个股的股票信息
# def getStockInfo(lst, stockURL, fpath):
#     for stock in lst:
#         url = stockURL + stock + ".html"
#         html = getHTMLText(url)
#         try:
#             if html=="":
#                 continue
#             infoDict = {}
#             soup = BeautifulSoup(html, 'html.parser')
#             stockInfo = soup.find('div', attrs = {'class':'stock-bets'})
#
#             name = stockInfo.find_all(attrs = {'class':'bets-name'})[0]
#             infoDict.update({'股票名称':name.text.split()[0], "股票代码":stock})
#
#             keyList = stockInfo.find_all('dt')
#             valueList = stockInfo.find_all('dd')
#             for i in range(len(keyList)):
#                 key = keyList[i].text
#                 val = valueList[i].text
#                 infoDict[key] = val
#
#             with open(fpath, 'a', encoding='utf-8') as f:
#                 print(fpath)
#                 f.write( str(infoDict) + '\n' )
#         except:
#             traceback.print_exc()
#             continue
#
# def main():
#     stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
#     stock_info_url = 'http://gupiao.baidu.com/stock/'
#     path = '/home/maosiyi/图片/b.txt'
#     slist = set()
#     getStockList(slist, stock_list_url)
#     getStockInfo(slist, stock_info_url, path)
#
# main()


#股票数据定向爬虫,优化
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, "GB2312")
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0], '股票代码':stock})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write( str(infoDict) + '\n' )
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'http://gupiao.baidu.com/stock/'
    output_file = '/home/maosiyi/文档/股票信息.txt'
    slist=[]
    # slist = set()
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()
