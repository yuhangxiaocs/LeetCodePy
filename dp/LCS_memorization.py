'''
    这个方法当然也是对的，但是就没有那么直观了，比如这个边界处理，就不是很优雅
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


'''
    这里采用的是比较符合直觉的方式，而不是倒序，很多地方喜欢用倒序哎，不知道为什么
    
    思路其实很简单，原问题是[1, m] 和 [1, n]的最长子串，假设从这个地方出发，发现a1 ==  b3
    那么问题就转换成 [2, m] 和 [4, n]的最长子串，结果在+1即可，为啥之前的都不考虑呢，是因为子串需要按序
'''


def lcs_v1(s1, s2, id1, id2, memo):
    # 这里其实也可以加到memo中，但是不加也可以，因为我们是直接返回答案的，所以memo只是个辅助工具
    if id1 == len(s1) or id2 == len(s2): return 0
    # 如果在备忘录中存在 直接返回就行 这样写实Python的简便写法，其实是搜索key=(id1, id2)是否在memo中；
    if (id1, id2) in memo:
        return memo[id1, id2]
    res = 0
    if s1[id1] == s2[id2]:
        res = 1 + lcs_v1(s1, s2, id1 + 1, id2 + 1, memo)
    else:
        res = max(lcs_v1(s1, s2, id1 + 1, id2, memo), lcs_v1(s1, s2, id1, id2 + 1, memo))
    memo[id1, id2] = res
    return res


if __name__ == '__main__':
    s1 = "xiddao"
    s2 = ""
    memo = {}

    print(lcs_v1(s1, s2, 0, 0, memo))
    # print(memo[0, 0])
    print(memo)
