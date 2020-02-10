'''
    dp[i][j]表示前i项（包含i）组合的和为j的个数

    当前项 它是由前两项推出来的
    dp[i][j] =  dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]

    若一直dp[i-1][j] 它为两项做出贡献
    dp[i][j+nums[i]] 和 dp[i][j - nums[i]]
'''


class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return None
        # dp[i][2001]
        dp = [[0 for i in range(2001)] for j in range(len(nums))]

        dp[0][-nums[0] + 1000] = 1
        dp[0][nums[0] + 1000] += 1

        # for i in range(1, len(nums)):
        #     for sum in range(-1000, 1001):
        #         # 每一行的两个都可以用前一行推出来
        #         if dp[i - 1][sum + 1000] != 0:
        #             dp[i][sum + 1000 + nums[i]] += dp[i - 1][sum + 1000]
        #             dp[i][sum + 1000 - nums[i]] += dp[i - 1][sum + 1000]

        '''
        Runtime: 2240 ms, faster than 5.03% of Python3 online submissions for Target Sum.
        Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Target Sum.
        
        换成这种循环 就奇慢无比 为什么
        '''
        for i in range(1, len(nums)):
            for sum in range(-1000, 1001):

                index1 = sum - nums[i] + 1000
                index2 = sum + nums[i] + 1000
                a = 0
                if index1 >= 0 and index1 < 2001:
                    if dp[i - 1][index1] != 0:
                        a = dp[i - 1][index1]

                b = 0
                if index2 >= 0 and index2 < 2001:
                    if dp[i - 1][index2] != 0:
                        b = dp[i - 1][index2]

                dp[i][sum + 1000] = a + b

        return dp[len(nums) - 1][S + 1000] if S <= 1000 else 0


if __name__ == '__main__':
    print(Solution().findTargetSumWays(
        [0, 38, 42, 31, 13, 10, 11, 12, 44, 16, 38, 17, 22, 28, 9, 27, 20, 35, 34, 39], 2))

    # for i in range(1, len(nums)):
    #     for sum in range(-1000, 1001):
    #         if dp[i - 1][sum + 1000] > 0:
    #             dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000];
    #             dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000];
