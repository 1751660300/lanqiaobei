# -*- coding:utf-8 -*-
n = int(input())
a = input().split(" ")


def i(s):
    return int(s)


if n < 2:
    print(a[0])
else:
    a.pop()
    a.sort(key=i)
    for b in a:
        print(b, end=' ')
# 问题：n大于1时，a的分割会多出一个空出来，所以要把列表的最后一个元素删除

# 技术：使用了列表的排序
#         想起了字符的提取   re  lxml bs4 jsonpath
