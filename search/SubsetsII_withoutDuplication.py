import itertools


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        # 去重要排序
        nums.sort()

        def dfs(nums, index, path, res):
            res.append(path[:])

            for i in range(index, len(nums)):
                # 这里是关键
                if i > index and nums[i] == nums[i - 1]: continue
                path.append(nums[i])
                dfs(nums, i + 1, path, res)
                path.pop()

        dfs(nums, 0, [], res)

        return res


if __name__ == '__main__':
    print(Solution().subsetsWithDup([4, 4, 4, 1, 4]))
