#!/usr/bin python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests, sys, importlib
importlib.reload(sys)    #编码转换


#类说明：下载《笔趣看》网小说《一念永恒》
#Parameters: 无
#Returns: 无
#Modify: 2018-02-26

class download(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names= []
        self.urls = []
        self.nums = 0

    #获取下载链接
    #Parameters: 无
    #Returns: 无
    #Modify: 2018-02-26
    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        bf = BeautifulSoup(html)
        all_bf = bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(all_bf[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[15:])
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    #获取章节内容
    #Parameters: target(下载链接)--string
    #Returns: content(章节内容)--string
    #Modify: 2018-02-26
    def get_contents(self,add):
        req = requests.get(url=add)
        html = req.text
        bf = BeautifulSoup(html)
        rs_bf = bf.find_all('div', class_ = 'showtxt')
        content = rs_bf[0].text.replace('\xa0'*8, '\n\n')
        return content

    #将爬取的文章内容写入文件
    #Parameters: name(章节名)--string、 content(小说内容)--string
    #Returns: 无
    #Modify: 2018-02-26
    def writer(self, name, path, content):
        write_flag = True
        with open(path, 'a', encoding = 'utf-8') as f:
            f.write(name + '\n')
            f.writelines(content)
            f.write('\n\n')


if __name__ == "__main__":

        dl = download()
        dl.get_download_url()
        print('《一年永恒》开始下载：')
        for i in range(dl.nums):
            dl.writer(dl.names[i],'一念永恒.txt', dl.get_contents(dl.urls[i]))
            sys.stdout.write('已下载：%.3f%%' % float(i/dl.nums) + '\r')
            sys.stdout.flush()
        print('《一年永恒》下载完成')


if __name__ == "__main__":

    dl = download()
    dl.get_download_url()
    print('开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '', dl.get_contents(dl.urls[i]))
        sys.stdout