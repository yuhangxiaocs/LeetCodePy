class Solution(object):

    def dfs(self, nums, index, cur, S):

        if index == len(nums):
            if cur == S:
                return 1
            return 0

        # 剪枝
        if cur + sum(nums[index:]) < S:
            return 0
        if cur - sum(nums[index:]) > S:
            return 0

        return self.dfs(nums, index + 1, cur + nums[index], S) + self.dfs(nums, index + 1, cur - nums[index], S)

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return None

        return self.dfs(nums, 0, 0, S)


if __name__ == '__main__':
    print(Solution().findTargetSumWays(
        [0, 38, 42, 31, 13, 10, 11, 12, 44, 16, 38, 17, 22, 28, 9, 27, 20, 35, 34, 39], 2))

'''
    [25,29,23,21,45,36,16,35,13,39,44,15,16,14,45,23,50,43,9,15], 32
    
    
'''
