'''
    好的思路：
    https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-:-)
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
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                flag = False
                j = i
                while j > start:

                    if nums[j] == nums[start]:
                        flag = True
                        break
                    j -= 1

                if flag: continue

                nums[start], nums[i] = nums[i], nums[start]
                shuffle(nums, start + 1, res)
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
