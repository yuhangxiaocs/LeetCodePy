class Solution(object):
    # 转换成cycle detection问题，使用弗洛伊德环路检测算法
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tortoise = nums[0]
        hare = nums[0]
        # 因为这里一定有环 所以用while True
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            if tortoise == hare: break

        p = tortoise
        q = nums[0]
        while p != q:
            p = nums[p]
            q = nums[q]
        return p
