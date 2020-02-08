class Solution(object):
    '''
        走过路过标记一下，对所有点dfs即可
    '''

    def dfs(self, grid, x, y):
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == '1':
            grid[x][y] = '#'
            self.dfs(grid, x + 1, y)
            self.dfs(grid, x - 1, y)
            self.dfs(grid, x, y - 1)
            self.dfs(grid, x, y + 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(Solution().numIslands(grid))
