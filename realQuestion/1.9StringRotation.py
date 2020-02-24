'''

    can use is substring methond once
'''


def isSubstring(s1, s2):
    '''

    :param s1:
    :param s2: check if s1 is substring of s2
    :return: True or False
    '''

    i = 0
    while i < len(s2):

        if s2[i] == s1[0]:
            j = 0
            while j < len(s1) and i + j < len(s2):
                if s2[i + j] != s1[j]: break
                j += 1
            if j == len(s1): return True
        i += 1
    return False


def isRotation(s1, s2):
    return isSubstring(s1, s2 + s2)


if __name__ == '__main__':
    s1 = 'waterbottle'
    s2 = 'erbottlewat'
    print(isRotation(s1, s2))
