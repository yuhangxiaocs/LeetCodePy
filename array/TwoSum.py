class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        # 因为可能有重复 所以这个循环只能用i做标识 而不能用num in nums算两次
        for i in range(len(nums)):
            if target - nums[i] in dic and i != dic[target - nums[i]]:
                res = [i, dic[target - nums[i]]]
                res.sort()
                return res
