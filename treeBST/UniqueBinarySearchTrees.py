class Solution(object):

    def numTrees(self, n):
        # G(n) = SUM(G(i)*G{n-1-i})
        # g(n) = f(1,n) + f(2, n) + ... + f(n, n)
        
        # 注意最关键的点在于 后面的g(n-i) 这是一种等效
        # 比如[1,2,3,4,5,6,7]
        # 计算 f(4, 7)的时候
        # 把数组分为两段 [1, 2, 3] & [5, 6, 7]
        # 理论上 g(n) 表示n序列长度的 是代表从1-n但是实际上
        # 我们求的只是一种组合方式 [5,6,7]和[1,2,3]是等价的
        
        # f(i, n) = g(i-1) * g(n-i)
        
        g = [0 for _ in range(n+1)]
        
        g[0] = g[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                g[i] += g[j-1] * g[i-j]
        
        return g[n]
        
# 原始方法
# 这里就没有考虑到lo,hi 实际上都是可以压缩到[1, 1+hi-lo]的 
# 因为计算的数量 是摆动的方式 所以只要大小顺序是那样 都可以
class Solution(object):
    def numTrees(self, n):
        dic = {}
        def helper(lo, hi):
            if (lo, hi) in dic: return dic[lo, hi]
            if lo >= hi: 
                dic[lo, hi] = 1
                return 1
            res = 0
            for i in range(lo, hi+1):
                res += helper(lo,i-1) * helper(i+1, hi)
            dic[lo, hi] = res
            return res
        
        return helper(1, n)
