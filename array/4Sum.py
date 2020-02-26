class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums: return
        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                t = target - nums[i] - nums[j]

                lo, hi = j + 1, len(nums) - 1

                while lo < hi:
                    if nums[lo] + nums[hi] == t:
                        res.add((nums[i], nums[j], nums[lo], nums[hi]))
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] > t:
                        hi -= 1
                    else:
                        lo += 1

        return res


if __name__ == '__main__':
    obj = Solution()

    print(obj.fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
#
# [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, 0, 0, 2], [-1, 0, 0, 1]]
# [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2]]
