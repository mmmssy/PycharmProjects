#!/usr/bin python3
# -*- coding: utf-8 -*-

#爬取baidu.com,python3.x
import requests
targeturl = 'http://www.baidu.com'
req = requests.get(url = targeturl)
print(req.text)

#python2.x
# import urllib2
# response = urllib2.urlopen("http://www.baidu.com")
# html = response.read()
# print html

