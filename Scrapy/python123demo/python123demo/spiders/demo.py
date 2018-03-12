# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    #allowed_domains = ["python123.io"]
    start_urls = (
        'http://www.python123.io/ws/demo.html',
    )

    def parse(self, response):   #对返回页面进行解析操作
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
             f.write(response.body)
        self.log('Saved file %s.' % fname)

