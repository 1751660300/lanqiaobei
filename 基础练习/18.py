# -*- coding:utf-8 -*-
# 0:zero, 1: one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, 10:ten,
# 11:eleven, 12:twelve, 13:thirteen, 14:fourteen, 15:fifteen, 16:sixteen, 17:seventeen,
# 18:eighteen, 19:nineteen, 20:twenty。
# 　　30读作thirty，40读作forty，50读作fifty
import re

dic_time = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty'}
data = input()


def trans(s):
    l_data = list()
    for i in re.findall('\d+|-\d+', s):
        l_data.append(int(i))
    return l_data


l_data = trans(data)


def get_h(m):
    h_tl = m % 10
    h_th = m / 10
    if m <= 20:
        return dic_time[m]
    else:
        return dic_time[int(h_th) * 10] + " " + dic_time[int(h_tl)]


def get_m(n):
    if n == 0:
        return "o'clock"
    m_tl = n % 10
    m_th = n / 10
    if n <= 20:
        return dic_time[n]
    else:
        return dic_time[int(m_th) * 10] + " " + dic_time[int(m_tl)]


print(get_h(l_data[0]), get_m(l_data[1]), sep=" ")
