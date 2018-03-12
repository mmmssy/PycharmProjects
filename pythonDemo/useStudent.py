#!/usr/bin/python 3
# -*- coding:utf-8 -*-

from Student import Students

Stu = []
while True:
    name = input('请输入姓名：\n>')
    score = input('请输入成绩：\n>')
    Stu.append(name, score)
    request = input('是否继续输入？（Y / N）\n>')
    if request == 'Y' or request == 'y':
        continue
    else:
        print('录入的信息如下：')
        for i in Stu:
            print('姓名：%s  成绩：%s  评价：%s' % (i.name, i.score, i.judscore()))
        break