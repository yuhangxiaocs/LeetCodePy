class Solution(object):
    # 简单的动态规划问题
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for i in range(m)]
        # init
        sum = 0
        for i in range(n):
            sum += grid[0][i]
            dp[0][i] = sum
        sum = 0
        for i in range(m):
            sum += grid[i][0]
            dp[i][0] = sum
        # main loop
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        print(dp[m - 1][n - 1])
        print(dp)

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    Solution().minPathSum(grid)
