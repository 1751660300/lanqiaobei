# -*- coding:utf-8 -*-
l = list()
i = int(input())
for j in range(i):
    l.append(input())
for j in l:
    print(oct(int(j, 16))[2::])

# 技术：进制转换函数：
#           十进制转2 4 8 16 ： int(string, int)
#           2 8 16 转十进制： bin() oct() hex()
