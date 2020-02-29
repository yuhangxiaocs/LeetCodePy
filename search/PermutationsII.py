'''
    最经典的版本
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def dfs(nums, pos, path):
            if pos == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == True: continue
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


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
