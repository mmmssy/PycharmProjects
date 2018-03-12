#~/usr/bin python3
# -*- coding:utf-8 -*-

# #获取html中所有的url链接
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("http://python123.io/ws/demo.html", "html.parser")
# for link in soup.find_all('a'):
#     print(link.get('href'))


# #中国大学排名定向爬虫
# import requests
# from bs4 import BeautifulSoup
# import bs4
#
# def getHTMLText(url):      #将url信息爬取下来,将其中html页面返回给其他程序
#     try:
#         r = requests.get(url, timeout = 30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         print("爬取失败")
#
#
# def fillUnivList(ulist, html):         #提取html信息中关键的数据,并且添到一个列表中
#     soup = BeautifulSoup(html, "html.parser")
#     for tr in soup.find('tbody').children:            #查找tbody标签,并且将他的孩子做一个遍历,每一个tr是一所大学对应的信息
#         if isinstance(tr, bs4.element.Tag):           #每一个标签的儿子标签中可能会出现字符串类型,过滤掉非标签类型的信息,检测tr标签的类型
#             tds = tr('td')              #对tr标签中的td标签做查询
#             ulist.append([tds[0].string, tds[1].string, tds[3].string])
#
#
# def printUnivList(ulist, num):
#     print("{:^10}\t{:^10}\t{:^15}".format("排名", "学校名称", "总分"))#格式化输出
#     for i in range(num):
#         u = ulist[i]   #打印表头
#         print("{:^10}\t{:^10}\t{:^15}".format(u[0], u[1], u[2]))
#
#
# def main():
#     uinfo = []
#     url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
#     html = getHTMLText(url)
#     fillUnivList(uinfo, html)
#     printUnivList(uinfo, 20)
# main()

#对中英文混排输出问题进行优化
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):      #将url信息爬取下来,将其中html页面返回给其他程序
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")


def fillUnivList(ulist, html):         #提取html信息中关键的数据,并且添到一个列表中
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:            #查找tbody标签,并且将他的孩子做一个遍历,每一个tr是一所大学对应的信息
        if isinstance(tr, bs4.element.Tag):           #每一个标签的儿子标签中可能会出现字符串类型,过滤掉非标签类型的信息,检测tr标签的类型
            tds = tr('td')              #对tr标签中的td标签做查询
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"        #format()中文对齐问题,{3}使用format函数的第三个变量进行填充,即使用中文空格填充
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))#格式化输出
    for i in range(num):
        u = ulist[i]   #打印表头
        print(tplt.format(u[0], u[1], u[2], chr(12288)))



def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
main()

