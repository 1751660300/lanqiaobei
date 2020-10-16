# -*- coding:utf-8 -*-
import re

# 输入一个整数n
data = input()


def trans(s):
    l_data = list()
    for i in re.findall('\d+|-\d+', s):
        l_data.append(int(i))
    return l_data


def show(a, b):
    for i in range(a):
        for k in range(min(i, b)):
            print(chr(65 + i - k), end='')
        for j in range(b - i):
            print(chr(65 + j), end='')
        print()


l_data = trans(data)
show(l_data[0], l_data[1])

# 问题1:字符与ASCII码的转换
# ord():字符转化为ASCII码
# chr():ASCII码转化为字符
# 问题2:for i in range(-5)会循环几次？
# 会循环0次
