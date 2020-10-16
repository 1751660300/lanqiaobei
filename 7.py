# -*- coding:utf-8 -*-
# 问题描述
# 　　如果一个序列的奇数项都比前一项大，偶数项都比前一项小，则称为一个摆动序列。即 a[2i]<a[2i-1], a[2i+1]>a[2i]。
# 　　小明想知道，长度为 m，每个数都是 1 到 n 之间的正整数的摆动序列一共有多少个。
# 输入格式
# 　　输入一行包含两个整数 m，n。
# 输出格式
# 　　输出一个整数，表示答案。答案可能很大，请输出答案除以10000的余数。
# 样例输入
# 3 4
# 样例输出
# 14
# 样例说明
# 　　以下是符合要求的摆动序列：
# 　　2 1 2
# 　　2 1 3
# 　　2 1 4
# 　　3 1 2
# 　　3 1 3
# 　　3 1 4
# 　　3 2 3
# 　　3 2 4
# 　　4 1 2
# 　　4 1 3
# 　　4 1 4
# 　　4 2 3
# 　　4 2 4
# 　　4 3 4
# 评测用例规模与约定
# 　　对于 20% 的评测用例，1 <= n, m <= 5；
# 　　对于 50% 的评测用例，1 <= n, m <= 10；
# 　　对于 80% 的评测用例，1 <= n, m <= 100；
# 　　对于所有评测用例，1 <= n, m <= 1000。
import re
import sys

sys.setrecursionlimit(1000000)  # 例如这里设置为十万
data = input()


def trans(s):
    l_data = list()
    for i in re.findall('\d+|-\d+', s):
        l_data.append(int(i))
    return l_data


l_inp = trans(data)
m = l_inp[0]  # 长度
n = l_inp[1]  # 范围
l_v = list()
for i in range(m):
    l_v.append(0)
if m == 1:
    print(n)
else:
    pass

res = 0


# 从第二位开始 即 x = 2
def f(x, l_v):
    global res
    if x == m:
        print(l_v)
        res += 1
        if res > 10000:
            res -= 10000
    else:
        if (x+1) % 2 == 0:
            for i1 in range(1, l_v[x - 1]):
                l_v[x] = i1
                f(x + 1, l_v)
        else:
            for i1 in range(l_v[x - 1] + 1, n + 1):
                l_v[x] = i1
                f(x + 1, l_v)


l = list()
for i in range(m):
    l.append(0)
for i in range(2, n + 1):
    l[0] = i
    f(1, l)
print(res)
