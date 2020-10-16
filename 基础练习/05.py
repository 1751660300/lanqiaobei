# -*- coding:utf-8 -*-
n = int(input())
i = 10000
j = 999999


def check(s):
    s = str(s)
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    k = 0
    for i in s:
        k = int(i) + k
    if k != n:
        return False
    else:
        return True


while i <= j:
    if check(i) is True:
        print(i)
    i += 1


# 问题：超时
# 解决：先判断是否为回文数
