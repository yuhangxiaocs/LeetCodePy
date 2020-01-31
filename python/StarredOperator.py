'''
    * 操作符可以实现很多高级的功能
'''

'''
    unpack elements
'''

# 任何可迭代的都可以这样赋值，只要左边的变量数量和右边一致就可以
s = 'xiao'
a, b, c, d = s
print(a, b, c, d, sep=' ')

# 用*操作符 可以实现解压特定的元素， 抛弃特定的元素
s = [1, 2, 3, 4, 5]
head, *mid, tail = s
print(head, mid, tail)
