import bisect


class Solution(object):
    # 思想很简单 除了第一个外 以后没必要全排序  只要使用插入排序就行了 复杂度是O(k)
    # 并且由于有序 可以使用二分查找来加快速度 从而达到对数时间复杂度

    # 92.89% 44.44%
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        n = len(nums)
        res = []
        # 使用sorted 不破坏原有的有序性
        window = sorted(nums[0:k])
        for i in range(k, n + 1):
            res.append((window[k // 2] + window[(k - 1) // 2]) / 2.0)
            if i == n: break
            index = bisect.bisect_left(window, nums[i - k])
            window.pop(index)
            bisect.insort_left(window, nums[i])
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
