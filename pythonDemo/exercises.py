#!/usr/bin python3
# -*- coding: utf-8 -*-

#No.1
# d = []
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if(i != j) and (j != k) and (k !=i):
#                 d.append([i,j,k])
# print(d)
# print('总数为：', len(d))

#No.2
# x = int(input('净利润：'))
# if x <= 100000:
#     y = x * 0.1
#     print('奖金总数为：', y, '元')
# elif 100000 < x <= 200000:
#     y = 10000 + (x - 100000) * 0.075
#     print('奖金总数为：', y, '元')
# elif 200000 < x <= 400000:
#     y = 10000 + 7500 + (x - 200000) * 0.05
#     print('奖金总数为：', y, '元')
# elif 400000 < x <= 600000:
#     y = 10000 + 7500 + 10000 + (x - 400000) * 0.03
#     print('奖金总数为：', y, '元')
# elif 600000 < x <= 1000000:
#     y = 10000 + 75000 + 10000 + 6000 + (x - 600000) * 0.015
#     print('奖金总数为：', y, '元')
# else:
#     y = 10000 + 7500 + 10000 + 6000 + 6000 + (x - 1000000) * 0.01
#     print('奖金总数为：', y, '元')


# num = int(input('净利润：'))
# obj = {100:0.01,60:0.015, 40:0.03, 20:0.05, 10:0.075, 0:0.1 }
# keys = obj.keys()
# keys.sort()     #只适用于python2
# keys.reverse()  #只适用于python2
# res = 0
# for i in keys:
#     if num > i:
#         res += (num - i) * obj.get(i)
#         num = i
# print'奖金总数为：', res, '万元'


# y = int(input('净利润：'))
# num = [100, 60, 40, 20, 10, 0]
# rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# rs = 0
# for i in range(0, 6):
#     if y > num[i]:
#         rs += (y-num[i]) * rate[i]
#         y = num[i]
# print('奖金总数为：', rs, '万元')

#No.3
# for m in range(168):
#     for n in range(168):
#         if (m + n) * (m - n) == 168:
#             x = n ** 2 - 100
#             print(x)


#No.4
year = input('请输入年份：')
month = input('请输入月份：')
day = input('请输入几号：')

days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if 0 < month <= 12:
    sum = days[]
