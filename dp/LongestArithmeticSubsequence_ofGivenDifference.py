class Solution(object):
    '''
        看了Lee215大神的一期视频是和这个类似的，但那个更难，没给difference

        其实算是动态规划了，但是这里并不一开始就想转移方程，而是从需求出发，用到什么设什么

        其实也是记忆化搜索的过程，求解当前情况时，利用已知结果
    '''

    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = {}
        for i in range(len(arr)):
            dp[arr[i]] = dp[arr[i] - difference] + 1 if arr[i] - difference in dp else 1
        return max(dp.values())
