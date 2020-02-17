'''
    https://leetcode.com/problems/longest-arithmetic-sequence/discuss/274611/JavaC++Python-DP
'''


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = {}
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                diff = b - a
                try:
                    dp[diff, j] = dp[diff, i] + 1
                except:
                    dp[diff, j] = 2

        return max(dp.values())
