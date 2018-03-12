#!/usr/bin python3
# -*- coding: utf-8 -*-

# name=input("What's your name?")
# print('My name is:',name)

# name = input()
# print('Hello,', name)

# print('I\nam\nmsy')
# print('''I
# am
# msy''')


# l=[['apple','google','microsoft'],['java','python','ruby','php'],['adam','bart','lisa']]
# print(l[0][0])
# print(l[1][1])
# # print(l[2][2])
# print(l[0][0]+'\n'+l[1][1]+'\n'+l[2][2])

# age=3
# if age>=18:
# 	print('your age is',age)
# 	print('adult')
# else:
# 	print('your age is',age)
# 	print('teenager')

# age=3
# if age>=18:
# 	print('adult')
# elif age>=6:
# 	print('teenager')
# else:
# 	print('kid')


# age=20
# if age<6:
# 	print('kid')
# elif age>=6:
# 	print('teenager')
# else:
# 	print('adult')

# a=0
# if a:
# 	print('True')


# a=input('How old are you?'+'\n')
# age=int(a)
# if age==22:
# 	print('Me too!')
# elif age<22:
# 	print('I\'m older than you~')
# else:
# 	print('I\'m younger than you~')



# x = input("haha")
# print x
# print x[0]

# import sys
# sys.exit(0)


# myhobby='swimming'
# a=raw_input('What\'s your favorite hobby?'+'\n')
# if a==myhobby:
# 	print('wow!What a coincidence~')
# else:
# 	print('cool!')
# import sys
# sys.exit(0)



# height=1.75
# weight=80.5
# BMI=weight/height**2
# rs='%.1f' % (weight/height**2)
# print(type(rs))
# print(rs+"1")
# print(rs)

# BMI=float(rs)
# print(type(BMI))
# print(BMI+1)
# print(BMI)
# import sys
# sys.exit(0)

# if BMI<18.5:
# 	print('过轻')
# elif BMI >= 18.5 and BMI < 25:
#     print('正常')
# elif BMI >= 25 and BMI < 28:
#     print('过重')
# elif BMI >= 28 and BMI <32:
#     print('肥胖')
# else:
#     print('严重肥胖')




# sum = 0
# for x in list(range(5)):
# 	sum = sum + x
# print(sum)

# sum = 0
# for x in range(5):
# 	sum = sum + x
# print(sum)

#

# sum = 0
# for x in range(101):
#     sum = sum + x
# print('0+1+2+...+100=',sum)

# t = (1,2,3)
# for x in t:
#     print(x)
#
# a = [1,2.3]
# for x in a:
#     print(x)


# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n -2
# print(sum)
#
#
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n -2
# print(sum)
#
# sum = 0
# m = 100
# while m > 0:
#     sum = sum + m
#     m = m - 2
# print(sum)
#
# sum = 0
# a = 0
# while a <= 100:
#     sum = sum + a
#     a = a + 2
# print(sum)
#
# L = ['Bart','Lisa','Adam']
# for i in L:
#     print 'Hello', i,'!'


# n = 1
# while n < 101 :
#     print(n)
#     n = n + 1
# print 'End'
# print('End')

# n = 1
# while n < 101 :
#     if n > 10 :
#         break
#     print(n)
#     n = n + 1
# print('End')


# n = 50
# while n <101 :
#     if n > 61:
#         break
#     print(n)
#     n = n + 2
# print('End')


# n = 0
# while n < 10 :
#     n = n + 1
#     if n % 2 == 0:
#         continue
#     print(n)

# n = 1
# rs = 1
# while n < 11:
#     rs = rs * n
#     n = n + 1
# print(rs)

#死循环
# n = 1
# sum = 0
# while n > 0:
#     sum = sum + n
#     n = n + 1
# print(sum)


# a = [1,2,3,4,5]
# print a[1]
# a = {111:'m',222:'s',333:'y'}
# print a[111]
# a[0] = 'msy'
# print(a)
# a = {'m':1,'s':2,'y':3}
# print(a)
# print a['m']
# a[0]='...'
# print(a)
# a['m']=111
# print a['m']
# a['mmm']=1
# print a



#把(1,2,3)放入dict中
# d = {(1,2,3):'aa',111:'bb',222:'cc'}
# print(d)
# print d[(1,2,3)]



#把(1,[2,3])放入dict中,问题4
# d = {'(1,[2,3])':1,'msy':2,111:3}
# print(d)
# print d['(1,[2,3])']
# print d['msy']
# print d[000]



#
# dd = {(1,[2,3]):1,'msy':2,111:3,'a':1,'b':2}
# print(dd)
# dd['cas']='aaa'
# print(dd)



#把（1,2,3）放入set中
# s = set([(1,2,3),'msy',True,123,'...'])
# print(s)




#把（1,[2,3]）放入set中，问题4
# s = set(['(1,[2,3])','msy',True,123,'...'])
# print(s)


#问题1，如何删除类似于多维数组的列表中的元素,如何删除abc[0][0]
# abc=[['你','好'],'msy',111]
# print abc[0][0]
# abc.pop(1)
# print(abc)


#问题5，如何向set中添加一个“可变”元组
# s = set([11,11,11,2,3])
# print s
# print s.add((1,2,3))
# s.add(('a',[1,2]))
# print(s)


# s = set([1,2,3,4,4,5])
# s.remove(4)
# print s


# s1 = set([1,2,3])
# s2 = set([2,3,4])
# a = s1 & s2
# b = s1 | s2
# print(a)
# print b
#
# d = {'mm':1,123:123}
# d.pop(123)
# print d


#把一个整数转换成十六进制表示的字符串
# n1 = 255
# n2 = 1000
# a = hex  #hex()十六进制转换
# print '255的十六进制表示为:',a(n1)
# print '1000的十六进制表示为:',a(n2)

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-7))


# def my_abs1(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('x类型不符合要求')
#     if x >= 0:
#         return x
#     else:
#         return -x
#     my_abs1(-7)


# def a(x):
#     if not isinstance(x,str):
#         raise TypeError('请输入正确的类型')
#     if x=='swimming':
#         return 'me too'
#     else:
#         return 'cool'

# def plus(a):
#    return a+10
# print(plus(1))
#

# def nop():
#     pass
#

# def judage(x):
#     if x >= 18:
#         pass
#     elif 15 < x < 18:
#         return x+1
#     else:
#         return -x
# print(judage(19))



#从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
# import math
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y + step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
# r = move(100, 100, 60, math.pi / 6)
# print(r)


#一元二次方程求解
# import math
# def quadratic(a,b,c):
#     if not isinstance(a,(int,float)):
#         raise TypeError('请输入正确的数值')
#     if not isinstance(b,(int,float)):
#         raise TypeError('请输入正确的数值')
#     if not isinstance(c,(int,float)):
#         raise TypeError('请输入正确的数值')
#     d = b * b - 4 * a * c
#     if a == 0:
#         if b == 0:
#             if c == 0:
#                 return '方程根为全体实数'
#             else:
#                 return  '方程无根'
#         else:
#             x1 = -c / b
#             x2 = x1
#             return x1,x2
#     else:
#         if d < 0:
#             return '方程无根'
#         else:
#             x1 = (-b + math.sqrt(d))/2/a
#             x2 = (-b - math.sqrt(d))/2/a
#             return x1,x2
# a = quadratic(2,3,1)
# print a
# print(quadratic(2,3,1))
# print(quadratic(1,3,-4))


# def pow(x):
#     return x * x
# print(pow(5))


# def pow(x, n):
#     s = 1
#     while(n > 0):
#         n = n - 1
#         s = s * x
#     return s
# print(pow(5,2))


# def pow1(x,n = 2):
#     s = 1
#     while(n > 0):
#         n = n - 1
#         s = s * x
#     return s
# print(pow1(5))
# print(pow1(5,2))
# print(pow1(5,3))

# def pow2(x, n):
#     s = x ** n
#     return s
# print(pow2(5,-2))


# def enroll(name, gender):
#     print 'name:', name
#     print 'gender:', gender
# enroll('msy','女')


# def enroll1(name,gender,age=6,city="Beijing"):
#     print 'name:', name
#     print 'gender:', gender
#     print 'age:', age
#     print 'city:', city
# enroll1('msy','女')
# enroll1('msy','女',22)
# enroll1('msy','女',22,'Hefei')
# enroll1('msy','女',city='Hefei')


# def add_end(L=[]):
#     L.append('End')
#     return L
# print add_end([1,2.3])
# print add_end([1,'msy','...',True])
# print add_end()
# print add_end()
# print add_end()

# def add_end1(L=None):
#     if L is None:
#         L = []
#     L.append('End')
#     return L
# print add_end1()
# print add_end1()

# def product(*number):
#     rs = 1
#     for i in number:
#         rs = rs * i
#     return rs
# print(product(1,2,3,4,5))

# def hello(greeting, *args):
#     if(len(args)==0):
#         print('%s!' % greeting)
#     else:
#         print('%s, %s!' % (greeting, ','.join(args)))
# hello('Hi')
# hello('Hi','Sarah')
# hello('Hi','A','B','C')
#
# name = ('AA', 'BB')
# hello('Hi',*name)



# def print_scores(**kw):
#     print('   Name   Score')
#     print('---------------')
#     for name,score in kw.items():
#         print('%6s   %4d' % (name, score))
# print_scores(AA=99, BB=98, CC=97)

# a = {'ZZ':94, 'XX':95 ,'CC':91}
# print_scores(**a)


# def print_info(name, *, gender, city='Hefei', age):
#     print('Personal Info')
#     print('-------------')
#     print('Name: %s' % name)
#     print('Gender: %s' % gender)
#     print('City: %s' % city)
#     print('Age: %s' % age)
#     print()
#
# print_info('AA','女', age=20)
# print_info('Bob', gender='male', age=20, city='Beijing')
# print_info('AA', gender='女', city='Beijing', age=20)


#阶乘n!=1x2x3x...xn
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# print(fact(5))

# def fact1(n):
#     return fact1_iter(n, 1)
#
# def fact1_iter(num, product):
#     if num == 1:
#         return product
#     return fact1_iter(num-1, num * product)
# print(fact1(3))


# 利用递归函数移动汉诺塔:
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '--->', c)
#     else:
#         move(n - 1, a, c, b)
#         move(1, a, b, c)
#         move(n - 1, b, a, c)
# move(4, 'A', 'B', 'C')

#取前2个元素
# l = ['msy', 'abc', 1123, '...']
# r = []
# n = 2
# for i in range(n):
#     r.append(l[i])
# print(r)
# print(l[0:3])
# print(l[:3])
# print(l[1:0])
# print(l[1:2])
# print(l[-1:])
# print(l[-2:])
# print(l[-2:-1])

# L = list(range(100))
# A = L[49:91]
# sum = 0
# for i in A:
#     sum = sum + i
# print(sum)

# z = list(range(100))
# print(z[11:20])
# print(z[-10::2])
# print(z[:10:3])
# print(z[::10])
# print(z[::])

# x = (0, 1, 2, 3)
# print(x[:1])
# print(x[-1:])
# print((0, 1, 2)[:3:2])
# print('ahfcishcnskmckjf'[::5])


# 去除字符串首尾的空格
# def trim(s):
#     if s[:1] != ' ' and s[-1:] != ' ':
#         return s
#     elif s[:1] == ' ':
#         return trim(s[1:])
#     else:
#         return trim(s[:-1])
# print(' 111 ')
# print(trim(' 111 '))
# print(' 111')
# print(trim(' 111'))
# print('111 ')
# print(trim('111 '))

# d = {'a':1, 'b':2, 'c':3}
# for key in d:
#     print(key)
# for value in d.values():
#     print(value)
# for k, v in d.items():
#     print(k,v)
# for key in 'abc':
#     print(key)

# for i,value in enumerate((1,2,3)):
#     print(i,value)

# for x, y in [(1,1), (2,2), (3,3)]:
#     print(x,y)


#使用迭代查找一个list中最小和最大值，并返回一个tuple：
# def findMinAndMax(L):
#     if len(L) > 0:
#         if len(L) == 1:
#             return(L[0],L[0])
#         else:
#             min = L[0]
#             max = L[0]
#             for v in L:
#                 while min > v:
#                     min = v
#                 while max < v:
#                     max = v
#             return ('最大值：',max,'最大值的下标为：',L.index(max),'最小值：',min,'最小值的下标为：', L.index(min))
#     else:
#         return(None, None)
# print(findMinAndMax([1,2,3,4,5,6]))


# L2 = []
# def change(L):
#     for i in L:
#         if isinstance(i,str):
#             L2.append(i.lower())
#     return L2
# print(change(['Hello', 'World', 18, 'Apple', None]))

#斐波拉契数列:1,1,2,3,5,8,13,21...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# #斐波拉契数列generator
# def g_fib(item):
#     i, a, b = 0, 0, 1
#     while i < item:
#         yield b
#         a, b = b, a + b
#         i = i + 1
#     return 'done'
# #使用for循环来迭代：
# for n in g_fib(6):
#     print(n)
# #捕获StopIteration错误,拿到返回值：
# g = g_fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break





# print(g_fib(4))

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 2
#     print('step 3')
#     yield 3
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))


# # #杨辉三角,zip()错位,sum()相加
# def triangles():
#     a = [1]
#     while True:
#         yield a
#         a = [ sum(i) for i in (zip([0] + a, a + [0]))]
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break
#
# #杨辉三角，综合
# def triangles1():
#     a = [1]
#     while True:
#         yield a
#         a.append(0)
#         a = [a[i - 1] + a[i] for i in range(len(a))]
# n = 0
# result = []
# for t1 in triangles1():
#     print(t1)
#     result.append(t1)
#     n = n + 1
#     if n == 10:
#         break
# if result == [
#     [1]
#     [1, 1]
#     [1, 2, 1]
#     [1, 3, 3, 1]
#     [1, 4, 6, 4, 1]
#     [1, 5, 10, 10, 5, 1]
#     [1, 6, 15, 20, 15, 6, 1]
#     [1, 7, 21, 35, 35, 21, 7, 1]
#     [1, 8, 28, 56, 70, 56, 28, 8, 1]
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过！')
# else:
#     print('测试不通过!')


# def add(x, y, f):
#     return f(x) + f(y)
# print(add(-3, -2, abs))

# from functools import reduce
# d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return d[s]
#     return reduce(fn, map(char2num, s))
# print(str2int('12345'))

# from functools import reduce
# d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
# def char2num(s):
#     return d[s]
# def str2int(s):
#     return reduce(lambda x, y:x * 10 + y, map(char2num, s))
# print(str2int('12345'))

# #利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
# def normalize(name):
#    name=name[0].upper()+name[1:].lower()
#    return name
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
#
# #利用for循环，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
# l1=[]
# def change(l):
#     for i in l:
#         if isinstance(i,str) and i[:1] != ' ':
#             l1.append(i[0].upper() + i[1:].lower())
#     return l1
#
# print(change(['abd','xxx']))

# #编写一个prod()函数，可以接受一个list并利用reduce()求积
# from functools import reduce
# def prod(L):
#     def chengfa(x, y):
#         return x * y
#     return reduce(chengfa, L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# #编写一个prod()函数，可以接受一个list并利用lambda(),reduce()求积
# from functools import reduce
# def prod(L):
#     return reduce(lambda x, y : x * y, L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# #利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
#方法一：
# from functools import reduce
# DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
# def str2float(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     n = len(s) - 1 - s.find('.')
#     s = s.replace('.', '')
#     return reduce(fn, map(char2num, s)) / 10**n
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# #方法二：
# from functools import reduce
# def str2float(s):
#     def a(x,y):
#         return x*10 + y
#     def b(x,y):
#         return x/10 + y
#     def char2int(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     i = s.find('.')
#     return (reduce(a,map(char2int,s[:i])) + reduce(b,map(char2int,s[-1:i:-1]))/10)

# #利用lambda()函数简化字符串转浮点数
# from functools import reduce
# DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
# def char2num(s):
#     return DIGITS[s]
# def str2float(s):
#     n = len(s) - 1 - s.find('.')
#     s = s.replace('.', '')
#     return reduce(lambda x, y: x * 10 + y,map(char2num, s)) / 10**n
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# #filter求素数
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# def _not_divisible(n):
#     return lambda x: x % n >0
# def primes():
#     yield 2
#     it = _odd_iter()  #初始序列
#     while True:
#         n = next(it)  #返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it)  #构造新序列
# a = primes()
# for n in a:
#     if n < 1000:
#         print(n)
#     else:
#         break

#filter求回数
# #方法一：
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
# output = list(filter(is_palindrome, range(1,1000)))
# print('1000以内的质数有：', output)

# #方法二：
# def is_palindrome1(n):
#     s = str(n)
#     for i in range(0, len(s)):
#         if s[i] == s[len(s) - 1 - i]:
#             return True
#         else:
#              return False
# rs = list(filter(is_palindrome1, range(1,200)))
# print('200以内的质数有：', rs)

# #用一组tuple表示学生名字和成绩：t = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# t = [('Bob',75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# #按名字排序
# def by_name(t):
#     return t[0]
# L2 = sorted(t, key = by_name)
# print(L2)

# #按成绩排序
# #方法一：
# def by_score(t):
#     return t[1]
# L3 = sorted(t, key = by_score, reverse = True)
# print(L3)
# #方法二：
# def by_score1(t):
#     return -t[1]
# L4 = sorted(t, key = by_score1)
# print(L4)


#函数作为返回值
# def calc_sum(*agrs):
#     sum = 0
#     for i in agrs:
#         sum = sum + i
#     return sum
# print(calc_sum(1,2,3))

# def lazy_sum(*agrs):
#     def sum():
#         rs = 0
#         for i in agrs:
#             rs = rs + i
#         return rs
#     return sum
# f = lazy_sum(1,2,3)
# print(f)
# print(f())

# f1 = lazy_sum(1,2,3)
# f2 = lazy_sum(1,2,3)
# f1 == f2

#匿名函数
# a = list(map(lambda x:x * x, [1, 2, 3, 4, 5, 6]))
# print(a)

# f = lambda x : x * x
# print(f)
# print(f(5))

# def build(x,y):
#     return lambda:x * x + y * y
# print(build(1,2)())

# L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
# print(L)

#偏函数
# def f(x, base = 2):
#     return int(x, base)
# print(f('1'))
# print(f('10'))


# import functools
# fn = functools.partial(int, base=2)
# print(fn('10'))
# print(fn('10', base=8))
# print(fn('10', base=16))

# kw = {'base':16}
# print(fn('10', **kw))

# y = functools.partial(max)
# args = (1,2,3,4,5,6,7,8,9)
# print(y(*args))

# def test(a = 1, b = 2):
#     return a + b
# print(test())
# print(test(7, 8))

# import functools
# new_test = functools.partial(test, a = 3, b = 4)
# print(new_test())
# print(new_test(a = 7, b = 8))

# from functools import partial
# from operator import add
# new_add = partial(add,3)
# print(new_add(1))
# print(new_add(7))


# #作用域
# def _private1(name):
#     return 'Hi, %s' % name
# def _private2(name):
#     return 'Hello, %s' % name
# def greeting(name):
#     if len(name) > 3:
#         return _private1(name)
#     else:
#         return _private2(name)
# print(greeting('snfiknk'))

# a1 = {'name':'Michael', 'score':98}
# a2 = {'name':'Bob', 'score':99}
# def rs(a):
#     print('%s : %s' % (a['name'], a['score']))
# rs(a1)

# class Stu(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def rs(self):
#         print('%s : %s' % (self.name, self.score))
# Vava = Stu('Vava',80)
# Lisa = Stu('Aber',90)
# Vava.rs()
# Lisa.rs()

# class Student(object):
#
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def getInfo(self):
#         print('%s : %s, %s'  % (self.name, self.age, self.score))
#
#     def getLevel(self):
#         if self.score > 95:
#             return 'A'
#         elif self.score > 80:
#             return 'B'
#         else:
#             return 'C'
#
#
# Bob = Student('Bob',18, 96)
# Ana = Student('Ana',20, 87)
# Cindy = Student('Cindy', 22, 50)
# Bob.getInfo()
# print(Bob.name,':',Bob.getLevel())


# class testStu(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_Info(self):
#         print('姓名：%s, 分数：%s' % self.name, self.score)
#
# a = testStu('msy',98)
# print(a.name)
# a.name = '小红'
# a.score = 100
# print(a.name, a.score)

# class testStudent(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_Info(self):
#         print('姓名：%s, 分数：%s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#         if 0 <= score <= 100:
#            self.__score = score
#         else:
#             raise ValueError('bad score!')
#
# b = testStudent('小明', 88)
# print(b.get_name(),':',b.get_score())
# b.set_score(99)
# print(b.get_name(),':',b.get_score())
# print(b._testStudent__name)
# print(b._testStudent__score)
# b.__name = '小王'
# print(b.__name)
# print(b.get_name())
# print(b.print_Info())


# class Student1(object):
#
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self, gender):
#         # if gender == 'female' or gender == 'male':
#         if gender in ['male', 'female']:
#             self.__gender = gender
#         else:
#             raise ValueError('bad gender!')
#
#     def print_info(self):
#         print('姓名：%s, 性别：%s' % (self.name, self.__gender))
#
# bart = Student1('Bart', 'male')
# bart.set_gender('female')
# print(bart.get_gender())
# print(bart._Student1__gender)
# bart.Student1__gender = 'male'
# print(bart._Student1__gender)

# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# def run_twice(animal):
#     animal.run()
#     animal.run()

# run_twice(Animal())


# class Dog(Animal):
#     pass


# class Cat(Animal):
#     pass

# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()

# class Dog1(Animal):
#     def run(self):
#         print('Dog is running...')
#     def eat(self):
#         print('Dog is eating...')
# run_twice(Dog1())


# class Cat1(Animal):
#     def run(self):
#         print('Cat is running...')
#     def eat(self):
#         print('Cat is eating...')
# dog1 = Dog1()
# dog1.run()
# cat1 = Cat1()
# cat1.run()

# class Other(object):
#     def run(self):
#         print('other is running...')
# other1 = Other()
# other1.run()
# run_twice(other())

# a = list()
# b = Animal()
# c = Dog()
# d = Other()
# if isinstance(d, Animal):
#     print('True')
# else:
#     print('False')

# class Animals(object):
#     def eating(self):
#         print('Animal is eating...')
#
# class Cow(Animals):
#     def eating(self):
#         print('Cow is eating...')
#
# class NaiNiu(Cow):
#     def eating(self):
#         print('NaiNiu is eating...')
#
# a = Animals()
# b = Cow()
# c = NaiNiu()
#
# if isinstance(c, Cow):
#     print(True)
# else:
#     print(False)
#
# if isinstance(c, Animals):
#     print(True)
# else:
#     print(False)
#
# if isinstance(c, Cow) and isinstance(c, Animals):
#     print(True)
# else:
#     print(False)
#
# if isinstance(b, NaiNiu):
#     print(True)
# else:
#     print(False)

# class Student():
#     def __init__(self):
#         self.__age = 1
#     def grade(self):
#         print('nsnvisnvi')
#     def getage(self):
#         return self.__age
#
# student = Student()
# tmp = getattr(student, 'getage')
# setattr(student, 'y', lambda x:x + 1)
# print(hasattr(student, 'y'))
# temp = getattr(student, 'y')
# print(temp(2))
# student.grade()


# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#     def add(self):
#         return self.x + self.x
#     def sub(self):
#         return self.x - self.x
#     def pow(self):
#         return self.x * self.x
#     def div(self):
#         return self.x / self.x
#
# a = MyObject()
# def run(x):
#     inp = input('method\n>')
#     if hasattr(a, inp):
#         fun = getattr(a,inp)
#         print(fun())
#     else:
#         setattr(a, inp, lambda x: x + 1)
#         fun = getattr(a, inp)
#         print(fun(x))
# run(a)

# class Abc(object):
#     def __init__(self, name):
#         self.name = name
# a = Abc('Bob')
# print(a.name)
# a.score = 90
# print(a.score)

# class Yyy(object):
#     name = 'www'
# b = Yyy()
# print(b.name)
# print(Yyy.name)
# b.name = 'xxx'
# print(Yyy.name)
# print(b.name)
# del b.name
# print(b.name)

# class Student(object):
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1
#
# v = Student('小一')
# print(v.name)
# print(Student.count)
# d = Student('小野人')
# print(d.name)
# print(Student.count)
# c = Student('小三')
# print(Student.count)

# #正则表达式
# import re
# test = '_fj51_'
# a = '400-1234567'
# if re.match(r'[a-zA-Z\_][a-zA-Z\_]*', test):
#     print('OK')
# else:
#     print('Wrong')
# if re.match(r'^\d{3}\-\d{1,7}', a):
#     print('Y')
# else:
#     print('N')

# import re
# def is_valid_email(addr):
#     if re.fullmatch(r'^[a-zA-Z\.]+@\w+.\w+', addr):
#         print('ok')
#     else:
#         print('Wrong')
# is_valid_email('someone@gmail.com')
# is_valid_email('bill.gates@microsoft.com')
# is_valid_email('bob#example.com')
# is_valid_email('mr-bob@example.com')

# import re
# def name_of_email(add):
#     res = re.match(r'^<?([\w\s]+)>?\s*\w*@\w+.\w+', add)
#     res1 = re.match(r'(<?)([\w\s]+)(>?)([\s\w]*)@(\w+).(\w+)', add)
#     if res1:
#         return res1.group(2)
#     else:
#         return False
# print(name_of_email('<Tom Paris> tom@voyager.org'))
# print(name_of_email('tom@voyager.org'))

# import re
# def wangyiname(name):
#     result = re.match(r'([a-zA-Z][0-9a-zA-Z\_]{6,18})@([0-9a-zA-Z]+).([a-z]{1,3})',name)
#     if result:
#         return True
#     else:
#         return False
# print(wangyiname('dsfevj@fjvnk.com'))


# class Student(object):
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise  ValueError('score must between 0 ~ 100!')
#         self.__score = value
#
# s = Student()
# s.score = 60
# print(s.score)

# class Stu(object):
#
#     @property
#     def birth(self):
#         return self.__birth
#
#     @birth.setter
#     def birth(self, value):
#         self.__birth = value
#
#     @property
#     def age(self):
#         return 2018 - self.__birth
#
# s = Stu()
# s.birth = 1
# print('age=', s.age)

# class Screen(object):
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         self.__width = width
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         self.__height = height
#
#     @property
#     def resolution(self):
#         return self.__width * self.__height
#
# a = Screen()
# a.width = 1024
# a.height = 768
# print('resolution = ', a.resolution)
# if a.resolution == 786432:
#     print('Success')
# else:
#     print('Fail')

# try:
#     print('try...')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:'. r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

print('hello')







