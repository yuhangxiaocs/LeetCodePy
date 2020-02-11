class Solution(object):

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        nums.insert(0, 1)
        nums.append(1)

        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for l in range(1, n + 1):
            for i in range(1, n + 2 - l):
                j = i + l - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + nums[k] * nums[i - 1] * nums[j + 1])

        return dp[1][n]


if __name__ == '__main__':
    print(Solution().maxCoins([3, 1, 5, 8]))
