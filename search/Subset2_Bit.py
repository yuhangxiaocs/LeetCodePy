

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        for comb in range(1 << n):
            path = []
            for i in range(n):
                if comb & (1 << i):
                    path.append(nums[i])
            res.append(path)

        return sorted(res, key=lambda x: len(x))


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
