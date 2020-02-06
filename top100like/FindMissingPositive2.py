class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

            print(i, nums)
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1


if __name__ == '__main__':
    obj = Solution()
    nums = [3, 4, -1, 1]
    print(nums)
    obj.firstMissingPositive(nums)
