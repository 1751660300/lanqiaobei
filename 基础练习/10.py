# -*- coding:utf-8 -*-
import re

# 输入一个整数n
n = int(input())
# 输入n个数
data = input()


# 输入的字符串转换为数列表
def trans(s):
    l_data = list()
    for i in re.findall('\d+|-\d+', s):
        l_data.append(int(i))
    return l_data


# 求总和
def h(l):
    result = 0
    for i in l:
        result += i
    return result


r_data = trans(data)

r_data.sort()
# print(r_data)
print(r_data[n - 1])
print(r_data[0])

print(h(r_data))

# 问题：先输出大数
