#!/usr/bin/python 3
# -*- coding: utf-8 -*-

' a test module '     #表示模块的文档注释

__author__ = 'Lori Mao'   #__author__变量 把作者写进去

import sys

def test():
    args = sys.argv   #argv变量用list存储了命令行的所有参数.aggv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too much arguments!')

if __name__ == '__main__':
    test()