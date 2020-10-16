# -*- coding:utf-8 -*-
i = 1000
j = 9999


def check(s):
    s = str(s)
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    else:
        return True


while i <= j:
    if check(i) is True:
        print(i)
    i += 1