class Solution(object):
    def __init__(self):
        self.nums = []
        self.used = []
        self.res = []
        self.tmp = []

    def p(self, index):
        if index == len(self.nums):
            # 用浅拷贝
            self.res.append(self.tmp[:])
            return
        for i in range(len(self.used)):
            if not self.used[i]:
                self.tmp[index] = self.nums[i]
                self.used[i] = 1
                self.p(index + 1)
                self.used[i] = 0

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.used = [0] * len(nums)
        self.tmp = [0] * len(nums)
        self.p(0)
        return self.res



if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
    nums = [1, 2, 3]
    print(nums[0:1])
    print(nums[:1] + nums[1 + 1:])
