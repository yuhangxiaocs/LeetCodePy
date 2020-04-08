# 标准的binary search [L, R)实现 
# 第一个版本好些 也就是说 如果中间检测到了 就提前退出 

# 所以那个G(m)的框架前面有一步就是check F(m)也就是说特定题目中满足条件可以提前退出
# 但是凡是涉及到lower bound这种的 是不可以提前退出的


class Solution(object):
    def search(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target: return mid
            if nums[mid] >= target:
                hi = mid
            else: lo = mid + 1
        return -1 
        
# 没必要的版本 直接在中间检查就可以了
class Solution(object):
    def search(self, nums, target):

        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid
            else: lo = mid + 1
        return -1 if lo==len(nums) or nums[lo]!=target else lo
