class Solution(object):
    '''
        记忆化搜索
    '''

    def dfs(self, nums, index, cur, S, mem):
        if index == len(nums):
            if cur == S:
                return 1
            return 0

        # 如果已经计算出来
        if (index, cur) in mem:
            return mem[index, cur]

        a = self.dfs(nums, index + 1, cur + nums[index], S, mem)
        b = self.dfs(nums, index + 1, cur - nums[index], S, mem)
        mem[index, cur] = a + b

        return mem[index, cur]

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return None
        # 先列后行
        mem = {}
        # print(mem)
        return self.dfs(nums, 0, 0, S, mem)


if __name__ == '__main__':
    print(Solution().findTargetSumWays(
        [0, 38, 42, 31, 13, 10, 11, 12, 44, 16, 38, 17, 22, 28, 9, 27, 20, 35, 34, 39], 2))

'''
    [25,29,23,21,45,36,16,35,13,39,44,15,16,14,45,23,50,43,9,15], 32
    
    
'''
