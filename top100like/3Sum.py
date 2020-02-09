class Solution(object):
    '''
        good explanation: https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)
    '''

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            # 由于是从小到大排序 第一个如果都大于0 那肯定结果大于0 可以结束循环
            if nums[i] > 0: break
            # 防止重复 重复的就跳过
            if i > 0 and nums[i] == nums[i - 1]: continue

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] + nums[i] < 0:
                    lo += 1

                elif nums[lo] + nums[hi] + nums[i] > 0:
                    hi -= 1

                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    # 重复跳过 注意指针 lo + 1
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    # 重复跳过 注意指针 hi - 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    # 别忘了这个
                    lo += 1
                    hi -= 1

        return res
