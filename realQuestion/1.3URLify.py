'''
    replace space with '%20'
    从后往前替换，时间复杂度O(N)

    solution
    通用解法就是这样 从后往前扫 避免覆盖问题 因此只需要one pass
'''


def urlify(s, length):
    '''

    :param s: input string wit enough space
    :param length: the length of the string to be processed
    :return:  the result
    '''
    s = list(s)
    space = 0

    for i in range(length):
        if s[i] == ' ': space += 1

    j = length + space * 2 - 1
    i = length - 1

    # 添加一个i！=j的判断 当i=j的时候说明已经可以结束了
    while i >= 0 and j != i:

        if s[i] == ' ':
            s[j - 2], s[j - 1], s[j] = '%', '2', '0'
            j -= 3
        else:
            s[j] = s[i]
            j -= 1
        i -= 1

    return "".join(s)


if __name__ == '__main__':
    print(urlify("Mr John Smith              ", 13))
    print(urlify("MrJohnSmith              ", 11))
