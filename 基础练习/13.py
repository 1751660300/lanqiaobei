# -*- coding:utf-8 -*-
m = int(input())


def pd(n):
    if n % 4 == 0 and n % 100 != 0:
        return "yes"
    elif n % 400 == 0:
        return "yes"
    else:
        return "no"


print(pd(m))
