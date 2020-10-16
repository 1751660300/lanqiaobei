# -*- coding:utf-8 -*-
# s = input()
# l = list(s)
# f = ""
# i = 0
# while i < len(l):
#     m = ord(l[i]) + 3
#     if m > 122:
#         m = m - 26
#     f += chr(m)
#     i += 1
# print(f)

# import re
#
# n = int(input())
#
# data = input()
#
#
# def trans(s):
#     l_data = list()
#     for i in re.findall('\d+|-\d+', s):
#         l_data.append(int(i))
#     return l_data
#
#
# j = 0
# l_da = trans(data)
# for i in range(n):
#     if ((i + 1) % l_da[0] != 0) and ((i + 1) % l_da[1] != 0) and ((i + 1) % l_da[2] != 0):
#         j += 1
# print(j)


import re
data = input()


def trans(s):
    l_data = list()
    for i in re.findall('\d+|-\d+', s):
        l_data.append(int(i))
    return l_data


l_da = trans(data)

i = 0
while l_da[0] > 0:
    pass



