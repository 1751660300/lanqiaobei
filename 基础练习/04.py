# -*- coding:utf-8 -*-
s = input()
print(hex(int(s)).swapcase()[2::])

# 问题：注意小写字母要转换为大写字母
# 解决： 使用str().swapase
