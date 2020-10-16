# -*- coding:utf-8 -*-
import re

# 输入整数n
n = int(input())
# 输入n个非负整数
data = input()
m = input()
l_data = re.findall('\d+', data)


def find(s, st):
    try:
        res = st.index(s)
    except:
        return -1
    else:
        return res + 1


print(find(m, l_data))

# 问题：列表的index方法找不到会抛出异常
#
