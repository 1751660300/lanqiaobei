# -*- coding:utf-8 -*-
import re

# 输入一个整数n
n = input()
data = input()


def trans(s):
    l_data = list()
    for i in re.findall('\d+|-\d+', s):
        l_data.append(int(i))
    return l_data


l_r = trans(data)
result = 0
while len(l_r) > 1:
    l_r.sort()
    i = l_r[0] + l_r[1]
    result = result + i
    l_r = l_r[2:]
    l_r.append(i)
print(result)
