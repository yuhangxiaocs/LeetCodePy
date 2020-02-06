class Solution(object):


    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    return nums[i]



if __name__ == '__main__':
    obj = Solution()

    print(obj.findDuplicate([1, 3, 4, 2, 2]))


# def findDuplicate(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     print(sum(nums))
#
#
#     return sum(nums) - sum(range(1, len(nums)))
