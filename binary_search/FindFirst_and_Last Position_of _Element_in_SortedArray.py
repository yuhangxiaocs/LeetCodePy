# 绝了 我这个版本真的不好理解 但还是对的...

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
    
# 这个版本是参考一个YouTube的思路 它的想法很“笨” 但绝对不会错，那就是在每次mid==target的时候更新一个flag变量
# 这样就可以让你忽略下标+1还是-1的问题，你只要确保不会miss中间的，以及循环可以正确退出即可



# personally the best version

class Solution(object):
    def searchRange(self, nums, target):
        def lower_bound(nums, target):
            lo ,hi = 0, len(nums)
            
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= target: hi = mid
                else: lo = mid + 1
            return lo
        
        def upper_bound(nums, target):
            lo ,hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target: hi = mid
                else: lo = mid + 1
            return lo
        
        lo, hi = lower_bound(nums, target), upper_bound(nums, target)
        
        return [lo, hi - 1] if lo != hi else [-1, -1]
