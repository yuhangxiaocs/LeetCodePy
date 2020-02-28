import itertools


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        for i in range(len(nums) + 1):
            res += itertools.combinations(nums, i)

        return res

    def subsets2(self, nums):

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
    print(Solution().subsets2([1, 2, 3]))
