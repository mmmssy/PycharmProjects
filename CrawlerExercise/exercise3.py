#~/usr/bin python3
# -*- coding:utf-8 -*-

# #爬取网页的通用代码框架
#
# import requests
#
# def getHtmlText(url):
#     try:
#         r = requests.get(url, timeout = 30)
#         r.raise_for_status()   #如果状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "状态异常"
#
# if __name__ == "__main__":
#     url = "http://www.baidu.com"
#     print(getHtmlText(url))


# #爬取京东商品数据
# import requests
# url = "https://item.jd.com/1279827.html"
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print("爬取失败")


# #爬取亚马逊商品信息,若返回的状态码不为200,则需利用代码模拟浏览器向网站发送请求,修改headers字段的相关信息
# import requests
# url = "https://www.amazon.cn/dp/B073L91FTR/ref=cngwdyfloorv2_recs_0/460-3698367-8489050?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=0CCS7HA90EF31D8JZ6DY&pf_rd_r=0CCS7HA90EF31D8JZ6DY&pf_rd_t=36701&pf_rd_p=19fc3fc8-b320-45dc-a7e8-b4ecd543eea8&pf_rd_p=19fc3fc8-b320-45dc-a7e8-b4ecd543eea8&pf_rd_i=desktop"
# try:
#     kv = {'User-Agent':'Mozilla/5.0'}  #构造键值对,重新定义user-agent内容,身份标识字段,修改header字段的相关信息
#     r = requests.get(url, headers = kv)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text)
# except:
#     print('爬取失败')


# #百度,360搜索,关键词提交,利用url向搜索引擎提交关键词
# #百度搜索
# import requests
# keyword = "Python"
# try:
#     kv = {'wd': keyword}
#     r = requests.get("https://www.baidu.com/s?wd=", params = kv)
#     print(r.request.url)
#     r.raise_for_status()
#     print(len(r.text))
# except:
#     print("爬取失败")


# #360搜索
# import requests
# keyword = "python"
# try:
#     kv = {'ie':keyword}
#     r = requests.get("https://www.so.com/s?ie=", params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     print(len(r.text))
# except:
#     print("爬取失败")


# #网络图片的爬取和存储
# import requests
# import os
# url = "https://awsbj0-cdn.fds-ssl.api.xiaomi.com/20160324-01-huami-homepage/uploads/banners/5a375e11dab5c.jpg"
# root = "/home/maosiyi/图片/"
# path = root + url.split('/')[-1]   #url链接的,以'/'分割的最后一部分,即jpg文件,path变量包含本地路径中的一个文件名称,该名称与网络路径最后一部分文件名称是相同的
# try:
#     if not os.path.exists(root):  #判断当前根目录是否存在
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

# #爬取动图
# import requests
# import os
# url = "https://pic1.qiyipic.com/common/lego/20180302/a9385e1624d04f84b4058cca8729cf5b.gif"
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
# except Exception as e:     #打印错误类型
#     print(e)
#     print("爬取失败")


# #IP地址归属地的自动查询
# import requests
# url = "http://ip.chinaz.com/"
# try:
#     r = requests.get(url + '182.92.67.167')
#     print(r.text[-500:])
#     print("爬取成功")
# except:
#     print("爬取失败")

# # #爬取视频
# import requests
# import os
# url = "http://mvideo.spriteapp.cn/video/2018/0304/d4ae5d161f9111e8b289842b2b4c75ab_wpcco.mp4"
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
#             print("保存成功")
#     else:
#         print("已经存在")
# except:
#     print("爬取失败")




