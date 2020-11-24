'''
    1005. Maximize Sum Of Array After K Negations
'''

def largestSumAfterKNegations(self, A, K):
    res = 0
    A.sort()  # nlogn
    i = 0
    # 计算出小于0的数
    negCount = len(filter(lambda x: x < 0 , A))
    # 如果有很多小于零的数 显然就是贪心的选择大的负数让它变成正的，这也是排序的原因
    if negCount >= K:
        return  -sum(A[:K]) + sum(A[K:])
    # 否则，首先把所有的数都变成正数，如果K-ngeCount为偶数 难就啥都不用变
    # 如果是奇数 那就选择一个绝对值最小的数，减去它的二倍即可
    # 使用 K&1判断奇偶比%快得多
    else:
        minAbs = min(map(abs, A))
        return  -sum(A[:negCount]) + sum(A[negCount:]) - 2 * minAbs * ((K-negCount)&1)
