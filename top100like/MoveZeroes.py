class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 这个方法几乎就是optimal的 时间是N 空间是常数
        # 如果再优化 就是在此基础上用交换法 也就是答案的写法 但是交换不也得费时间吗

        zeros = 0
        j = 0
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            nums[j] = num
            j += 1

        for i in range(zeros):
            nums[-1 - i] = 0
