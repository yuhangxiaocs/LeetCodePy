class Solution(object):
    # 由于超过了n/2 所以排序后一定在中间位置
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[int(len(nums) / 2)]
