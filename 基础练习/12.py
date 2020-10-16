# -*- coding:utf-8 -*-
for i in range(32):
    s = bin(i)[2:]
    for j in range(5 - len(s)):
        s = "0" + s
    print(s)

# 问题：进制转换
# bin()二进制  oct()八进制  hex()十六进制

