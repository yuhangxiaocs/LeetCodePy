'''
    given two string, check if one is the permutation of the other

    Solution
    还是要考虑字符集的 ASCII和Unicode 两种 可以默认是ASCII 但是要和interviewer说明

    1. 排序 和我想的一样
    2. 比较元素出现次数是否相等 还是和我想的一样 哈哈 不过 它是用数组 感觉还不如我用dictionary呢 因为用dictionary可以忽略字符集
    用数字的话还得考虑是不是ASCII
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
