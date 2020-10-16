# -*- coding:utf-8 -*-
# 资源限制
# 时间限制：1.0s   内存限制：512.0MB
# 问题描述
# 　　153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1*1*1+5*5*5+3*3*3。编程求所有满足这种条件的三位十进制数。
# 输出格式
# 　　按从小到大的顺序输出满足条件的三位十进制数，每个数占一行。
import math

i = 100
j = 999


def check(s):
    s = str(s)
    if math.pow(int(s[0]), 3) + math.pow(int(s[1]), 3) + math.pow(int(s[2]), 3) == int(s):
        return True


while i <= j:
    if check(i) is True:
        print(i)
    i += 1
