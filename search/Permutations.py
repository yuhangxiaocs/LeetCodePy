'''
    最经典的版本
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, pos, path):
            if pos == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])

                    dfs(nums, pos + 1, path)

                    path.pop()
                    visited[i] = False

        path, res = [], []

        visited = [False for _ in range(len(nums))]

        dfs(nums, 0, path)

        return res
