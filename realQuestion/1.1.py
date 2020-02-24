'''
    if a string has all unique characters
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
