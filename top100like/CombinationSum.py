class Solution(object):
    '''
        二叉树问题

        比如 [2, 3, 5] 8 问题

                             2
                  2          3         5
                2 3 5       3 5        5
               2

        就是每个元素 要么取 要么从下一个位置取  从下一个的时候 前面的就不能用了 以此避免重复
    '''
    def dfs(self, nums, index, curSum, target, path, res):
        if index >= len(nums) or curSum > target:
            return
        if curSum == target:
            res.append(path)
            return

        self.dfs(nums, index, curSum + nums[index], target, path + [nums[index]], res)
        self.dfs(nums, index + 1, curSum, target, path, res)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return
        res = []

        self.dfs(candidates, 0, 0, target, [], res)

        return res


if __name__ == '__main__':
    obj = Solution()
    res = obj.combinationSum([2, 3, 5], 8)

    print(res)
