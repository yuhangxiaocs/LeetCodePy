# [4,3,2,7,8,2,3,1]
# 0: 7 3 2 4 8 2 3 1
# 1: 7 2 3 4 8 2 3 1
# 2: 7 2 3 4 8 2 3 1
# 3: 7 2 3 4 1 2 3 8
#

# 元素一定能安排到合适的地方 因为范围在那里

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        n = len(nums)
        for i in range(n):
            if i + 1 != nums[i] and nums[i] - 1 != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        print(nums)

        for index, value in enumerate(nums):
            if index + 1 != value:
                res.append(index + 1)

        print(res)
        return res

    # 就是对每个数字 把它们对应位置的设置为负 然后每次取abs就行了
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    s = Solution()
    s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
