'''
    if a string has all unique characters

    首先要问字符串是ASCII的还是Unicode的 因为要保证程序的robust

    1. 如果都是ASCII 可以用一个128长度的数组 初始为0 然后每次有这个字母 就设置为1 如果设置的时候发现已经是1 那么就有重复了 就返回
    2. 把上述数组转化为bit vector 节省空间 实际上这两种都是常数空间
    3. 排序后 遍历 看相邻元素是否一样
    4. 把每个字符串和后面所有比较 平方时间

    靠 我理解错题意了 这里是问是不是独特的 我理解成唯一的了 啊啊啊！
'''


def isUnique(string):
    '''

    :param string:
    :return:
    '''
    if not string: return False

    x = string[0]

    for ch in string:
        if ch != x: return False
    return True


if __name__ == '__main__':
    print(isUnique("x"))
