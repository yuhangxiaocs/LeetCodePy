import bisect


class Solution(object):
    '''
        先排序 再从1开始向上找
    '''

    # 95.98%  55.88%
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 1
        while True:
            if i not in nums:
                return i
            i += 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4]

    print(1 in nums)
