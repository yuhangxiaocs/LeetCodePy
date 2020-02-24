'''
    given two string, check if one is the permutation of the other
'''


# 排序实现 T = N*logN S = 1
# def isPermutation(a, b):
#     return sorted(a) == sorted(b)

# O(N) O(N)
# def isPermutation(a, b):
#     tmp = list(a)
#     for ch in b:
#         try:
#             tmp.remove(ch)
#         except:
#             return False
#     return True


def isPermutation(a, b):
    dic = {}

    for ch in a:
        if ch in dic:
            dic[ch] += 1

        else:
            dic[ch] = 1

    for ch in b:
        if ch not in dic:
            return False
        else:
            dic[ch] -= 1

    for k, v in dic.items():
        if v != 0: return False
    return True


if __name__ == '__main__':
    print(isPermutation('abc', 'acdfb'))
