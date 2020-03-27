class Solution(object):
    def mySqrt(self, x):
        lo ,hi = 0, (x >> 1) + 1;
        while lo < hi:
            mid = (lo + hi) >> 1;
            if mid*mid >= x:
                hi = mid;
            else: lo = mid + 1;
        
        if lo*lo > x: return lo-1;
        return lo;
