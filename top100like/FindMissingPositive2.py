class Solution(object):
    def firstMissingPositive(self, nums):
        """for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i] 这这样写就错了 会死循环 因为会把nums[i]覆盖
                # 必须要先把index取出来

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        # 如果上面不满足 就是1-n都满了 所以返回n+1
        return n + 1


if __name__ == '__main__':
    obj = Solution()
    nums = [3, 4, -1, 1]
    print(nums)
    print(obj.firstMissingPositive(nums))
