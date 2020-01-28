class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.permutation(nums, 0, res)
        return res

    def permutation(self, nums, begin, res):
        if begin == len(nums):
            res.append(nums[:])
        for i in range(begin, len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.permutation(nums, begin + 1, res)
            nums[begin], nums[i] = nums[i], nums[begin]


if __name__ == '__main__':
    print(Solution().permute(['a', 'b', [1]]))
