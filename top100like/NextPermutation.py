class Solution(object):
    # 89%
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # edge case
        if not nums or len(nums) < 2:
            return

        i = len(nums) - 2
        # 注意两处等号 是为了 [1,1,5]这种情况
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        i = i + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 1, 5]
    obj.nextPermutation(nums)
    print(nums)
