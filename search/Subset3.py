import itertools


class Solution(object):
    def subsets(self, nums):
        res = []
        def dfs(nums, index, path, res):
            res.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(nums, i + 1, path, res)
                path.pop()
        dfs(nums, 0, [], res)
        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
