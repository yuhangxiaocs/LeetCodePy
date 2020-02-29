'''
    原理参见 Knuth洗牌算法

    区别在于 Knuth只考察一种情况 而这里取所有可能
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def shuffle(nums, start, res):

            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                shuffle(nums[:], start + 1, res)
                nums[start], nums[i] = nums[i], nums[start]

        res = []

        shuffle(nums, 0, res)

        return res


if __name__ == '__main__':
    print(Solution().permute([1, 1, 2, 2]))
