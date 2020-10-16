# -*- coding:utf-8 -*-
import re

data = input()


def trans(s):
    l_data = list()
    for i in re.findall('\d+|-\d+', s):
        l_data.append(int(i))
    return l_data


l_data = trans(data)
l = list()
for i in range(l_data[0]):
    data_s = input()
    l.append(trans(data_s))


def show():
    for i in range(min(l_data[0] + 1, l_data[1] + 1)):
        for j in range(l_data[0] - i):
            print(l[j][i], end=" ")
        for j in range(l_data[1] - i - 1):
            print(l[l_data[0] - i - 1][j + i + 1], end=" ")
        if l_data[1] - i - 1 > i:
            j = l_data[0] - i - 2
            while j >= i:
                print(l[j][l_data[1] - i - 1], end=" ")
                j -= 1
        if l_data[0] - i - 1 > i:
            j = l_data[1] - i - 2
            while j > i:
                print(l[i][j], end=" ")
                j -= 1
    # for (i = 0; i < (n + 1) / 2 & & i < (m + 1) / 2; i++)
    #
    #     for (j = i; j < m - i; j++)
    #     System.out.print(arr[j][i] + " ");
    #     for (j = i + 1; j < n - i; j++)
    #     System.out.print(arr[m - i - 1][j]+" ");
    #     if (n - i - 1 > i)
    #     for (j = m - i - 2; j >= i; j--)
    #     System.out.print( arr[j][n - i - 1]+" ");
    #     if (m - i - 1 > i)
    #     for (j = n - i - 2; j > i; j--)
    #     System.out.print( arr[i][j]+" ");


show()
