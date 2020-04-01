class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 1, sys.maxsize 
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * (mid+1) / 2 > n:
                hi = mid
            else: lo = mid + 1
        return lo - 1
