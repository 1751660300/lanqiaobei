# -*- coding:utf-8 -*-
import re

# 输入一个整数n
m_n = int(input())
c_map = list()


def trans(s):
    l_data = list()
    for i in re.findall('\d+|-\d+', s):
        l_data.append(int(i))
    return l_data


for i in range(m_n):
    data = input()
    c_map.append(trans(data))


# 1表示可以放皇后，0表示不可以放皇后，2表示放的白皇后，3表示放的黑皇后,4表示不能放白皇后，5表示不能放黑皇后
def fang_2(map, n, m):
    for x in range(n):
        for y in range(m):
            if map[x][y] != 0 and map[x][y] != 4:
                map[x][y] = 2
                check(map, x, y, 4)
                return map
    else:
        return 0


def fang_3(map, n, m, f_3_r):
    for x in range(n):
        for y in range(m):
            if map[x][y] != 0 and map[x][y] != 2 and map[x][y] != 5:
                map[x][y] = 3
                check(map, x, y, 4)
                return map
    else:
        return 0


def check(map, n, m, k):  # n表示横坐标，目标是纵坐标
    for x in range(1, n + 1):
        if map[n - x][m] == 1:
            map[n - x][m] = k
    for x in range(1, m_n - n):
        if map[n + x][m] == 1:
            map[n + x][m] = k
    for y in range(1, m + 1):
        if map[n][m-y] == 1:
            map[n][m - y] = k
    for y in range(1, m_n - m):
        if map[n][m + y] == 1:
            map[n][m + y] = k
    for x in range(1, min(n, m) + 1):
        if map[n - x][m - x] == 1:
            map[n - x][m - x] = k
    for x in range(1, min(m_n - n, m_n - m)):
        if map[n + x][m + x] == 1:
            map[n + x][m + x] = k
    for x in range(1, min(m_n - n, m + 1)):
        if map[n + x][m - x] == 1:
            map[n + x][m - x] = k
    for x in range(1, min(n + 1, m_n - m)):
        if map[n - x][m + x] == 1:
            map[n - x][m + x] = k
    return map


