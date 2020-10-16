# -*- coding:utf-8 -*-
# 资源限制
# 时间限制：1.0s   内存限制：256.0MB
# 问题描述
# 杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。
#
# 　　
# 它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。
#
# 　　
# 下面给出了杨辉三角形的前4行：
#
# 　　
#    1
#
# 　　
#   1 1
#
# 　　
#  1 2 1
#
# 　　
# 1 3 3 1
#
# 　　
# 给出n，输出它的前n行。
#
# 输入格式
# 输入包含一个数n。
#
# 输出格式
# 输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。
# 样例输入
# 4
# 样例输出
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 数据规模与约定
# 1 <= n <= 34。
n = int(input())


def display(l):
    for i in l:
        for j in i:
            print(j, end=" ")
        print()


l = [[1], [1, 1]]
if n < 2:
    print(1)
else:
    if n > 2:
        for i in range(n - 2):
            l1 = [1]
            l2 = []
            for j in range(int((i + 3) / 2)):
                l1.append(l[i + 1][j] + l[i + 1][j + 1])
            l2.extend(l1)
            if (i + 1) % 2 != 0:
                l2.pop()
            else:
                l2.pop()
                l2.pop()
            l2.reverse()
            l1.extend(l2)
            l.append(l1)
    display(l)

# 问题：n为偶数是l2要去掉最后两个元素，为基数时要去掉最后一个
