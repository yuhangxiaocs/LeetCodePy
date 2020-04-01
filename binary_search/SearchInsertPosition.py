# concise, efficient and easy-understanding
# using [L, R) to search
# which is equivalent to lower_bound in C++

class Solution(object):
    def searchInsert(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if (nums[mid] >= target): hi = mid
            else: lo = mid + 1
        return lo
            
    
    
