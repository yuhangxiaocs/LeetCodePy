class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        lo, hi = 0, len(nums) - 1
        reslo = reshi = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target <= nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1

        reslo = lo


        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target >= nums[mid]:
                lo = mid + 1
        reshi = hi
        return [reslo, reshi] if reslo <= reshi else [-1, -1]
