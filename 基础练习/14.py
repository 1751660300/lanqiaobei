# -*- coding:utf-8 -*-
# 输入一个整数n
n = int(input())

r = 1
for i in range(n):
    r *= (i + 1)

print(r)
