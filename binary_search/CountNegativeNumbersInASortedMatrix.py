# 每一行每一行统计
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def lower_bound(nums):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < 0:
                    hi = mid
                else:
                    lo = mid + 1
            return len(nums) - lo
        total = 0
        for row in grid:
            total += lower_bound(row)
        return total
        
# 优化一下 每一行统计的时候 列的下标不用移动回去，因为是列递减的，第一个位置如果小于0，那么
# 下一行一定也是小于0的，所以这就从n*logn 优化到 n + m 因为总共只会扫描一行
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        lo, hi = 0, len(grid[0]) - 1
        for row in grid:
            lo, hi = 0, min(hi + 1, len(grid[0]))
            while lo < hi:
                mid = (lo + hi) // 2
                if row[mid] < 0: hi = mid
                else: lo = mid + 1
            total += len(row) - lo
            
        return total
            
            
            
