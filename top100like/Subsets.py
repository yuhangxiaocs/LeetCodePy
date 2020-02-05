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

        for i in range(len(res)):
            res[i] = list(res[i])
        return res


if __name__ == '__main__':
    s = Solution()
    s.subsets([1, 2, 3])
    print(s.subsets([1, 2, 3]))
    res = []
    s.sub([1, 2, 3], 0, [], res)
    print(res)
