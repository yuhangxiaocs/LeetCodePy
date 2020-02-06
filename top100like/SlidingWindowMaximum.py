import bisect


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return None
        window = sorted(nums[:k])
        res = []
        # 这里要+1 是因为每次添加用的是上一次添加过的值
        for i in range(k, len(nums) + 1):
            res.append(window[-1])

            index = bisect.bisect_left(window, nums[i - k])

            if i == len(nums): break

            window.pop(index)

            bisect.insort_left(window, nums[i])

        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
