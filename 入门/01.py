# -*- coding:utf-8 -*-
# Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。
#
# 当n比较大时，Fn也非常大，现在我们想知道，Fn除以10007的余数是多少。
# 第一种
# a = 1
# b = 1
# c = int()
# n = int(input())
# if n >= 1 and n < 1000000:
#     if n < 2:
#         print(1)
#     else:
#         for i in range(n - 2):
#             c = a + b
#             a, b = b, c
#             print(c)

# 第二种
l = [1, 1, 0]
n = int(input())
if n >= 1 and n < 1000000:
    if n <= 2:
        print(1)
    else:
        for i in range(n - 2):
            l[2] = (l[0] + l[1])%10007
            l[0] = l[1]
            l[1] = l[2]
        print(l[2])



