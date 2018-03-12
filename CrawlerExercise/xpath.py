# /usr/bin python3
# -*- coding:utf-8 -*-

import requests
from lxml import etree

wb_data = """
           <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
"""

html = etree.HTML(wb_data)
# print(html)
result = etree.tostring(html)
# print(result.decode("utf-8"))
# html_data = html.xpath('/html/body/div/ul/li/a')
# for i in html_data:
#     print(i.text)

# html_data1 = html.xpath('/html/body/div/ul/li/a/@href')
# for i in html_data1:
#     print(i.split('.')[0])

# html_data2 = html.xpath('//li/a/text()')
# print(html_data2)
# for i in html_data2:
#     print(i)

# html_data3 = html.xpath('//li/a//@href')
# print(html_data3)
# for i in html_data3:
#     print(i.split('.')[0])

html_data4 = html.xpath('//li/a[@href = "link2.html"]')
print(html_data4)
for i in html_data4:
    print(i.text)

html_data5 = html.xpath('//li[last()]/a/text()')
print(html_data5)
for i in html_data5:
    print(i)