#!/usr/bin python3
# -*- coding: utf-8 -*-


# #No.1 获取网页数据
# import requests
# target = 'http://www.biqukan.com/1_1094/5403177.html'
# req = requests.get(url=target)
# print(req.text)


# #No.2 利用BeautifulSoup获取指定数据
# import requests
# from bs4 import BeautifulSoup
# target = 'http://www.biqukan.com/1_1094/5403177.html'
# req = requests.get(url=target)
# html = req.text
# bf = BeautifulSoup(html)
# content = bf.find_all('div', class_= 'showtxt')
# print(content.string)


# #No.3 利用BeautifulSoup获取指定数据并去除div、br、空格等,获取具体章节的内容
# import requests
# from bs4 import BeautifulSoup
# target = 'http://www.biqukan.com/1_1094/5403177.html'
# req = requests.get(url=target)
# html = req.text
# bf = BeautifulSoup(html)
# content = bf.find_all('div', class_ = 'showtxt')
# print(content[0].text.replace('\xa0'*8,'\n\n'))     #\xa0是不间断空白符 &nbsp



# import requests
# from bs4 import BeautifulSoup
# target = 'http://www.biqukan.com/1_1094/'
# req = requests.get(url=target)
# html = req.text
# bf = BeautifulSoup(html)
# content = bf.find_all('div', class_ = 'listmain')
# print(content[0])

# #获取章节名和对应的链接
# import requests
# from bs4 import BeautifulSoup
# server = 'http://www.biqukan.com/'
# target = 'http://www.biqukan.com/1_1094/'
# req = requests.get(url=target)
# html = req.text
# bf = BeautifulSoup(html)
# chapters = bf.find_all('div', class_ = 'listmain')
# a_bf = BeautifulSoup(str(chapters[0]))
# a = a_bf.find_all('a')
# for each in a:
#     print(each.string, server + each.get('href'))

# import requests
# from bs4 import BeautifulSoup
# server = 'http://www.biqukan.com/'
# target = 'http://www.biqukan.com/1_1094/'
# req = requests.get(url=target)
# html =req.text
# bf = BeautifulSoup(html)
# chapters = bf.find_all('div', class_ = 'listmain')
# a_bf = BeautifulSoup(str(chapters[0]))
# a = a_bf.find_all('a')
# for each in a :
#     print(each.string, server + each.get('href'))




