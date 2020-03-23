class Solution(object):

    # 最后总是返回lo
    def searchInsert(self, nums, target):
        if not nums: return 
        mid, lo, hi = 0, 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else: return mid      
        return mid + 1 if lo > mid else mid
            
    
