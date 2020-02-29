'''
    原理参见 Knuth洗牌算法

    区别在于 Knuth只考察一种情况 而这里取所有可能
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def shuffle(nums, start, res):
            if start == len(nums):
                res.append(nums)
                return

            for i in range(start, len(nums)):
                if i > start and nums[start] == nums[i]: continue
                # if i > start and nums[i] == nums[i - 1]: continue

                nums[start], nums[i] = nums[i], nums[start]
                shuffle(nums[:], start + 1, res)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        shuffle(nums, 0, res)
        return res


if __name__ == '__main__':
    nums = [-1, 2, 0, -1, 1, 0, 1]
    nums = [1, 1, 2]
    res = Solution().permuteUnique(nums)

    for r in res:
        print(r)
