class Solution(object):
    '''
        这个做法时间复杂度是n 空间为常数

        思路是这样的，由于他的数字范围都是正数
        遍历每个元素，把这个元素对于的下标的元素变成负数 负数就标记为 有这个个数 如果下次再设置此下标元素
        发现它是负数 就说明之前已经有一个数 这就是重复了 而且题目说 只重复一次 所以就找到了答案

        但是不太满足题目的要求 题目要求must not modify the inputs 所以这个方法虽然也很快 但是只提供了一种思路而已
    '''

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            index = abs(nums[i])

            if nums[index - 1] < 0:
                return index

            nums[index - 1] = -nums[index - 1]


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
