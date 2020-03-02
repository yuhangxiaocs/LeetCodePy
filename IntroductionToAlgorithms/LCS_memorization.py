'''
    
'''


def lcs(s1, s2, l1, l2, mem):
    if not (l1 + 1) or not (l2 + 1): return 0
    if (l1, l2) in mem:
        return mem[l1, l2]
    if s1[l1] == s2[l2]:
        mem[l1, l2] = lcs(s1, s2, l1 - 1, l2 - 1, mem) + 1
    else:
        a = lcs(s1, s2, l1 - 1, l2, mem)
        b = lcs(s1, s2, l1, l2 - 1, mem)
        mem[l1, l2] = max(a, b)

    return mem[l1, l2]


if __name__ == '__main__':
    s1 = "xiddao"
    s2 = ""
    mem = {}
    print(lcs(s1, s2, len(s1) - 1, len(s2) - 1, mem))
    print(mem)
