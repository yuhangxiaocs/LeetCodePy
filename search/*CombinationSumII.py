'''
    Runtime: 20 ms, faster than 99.75% of Python online submissions for Combination Sum II.
    Memory Usage: 11.8 MB, less than 74.19% of Python online submissions for Combination Sum II.
'''


class Solution(object):

    def dfs(self, nums, index, target, path, res):
        if target == 0:
            res.append(path[:])  # 注意这里哦 如果不这样拷贝 那就是错了
            return

        for i in range(index, len(nums)):
            # 在这里和在开头剪枝都可以
            if nums[i] > target: break

            # 这里是最大的区别
            if i > index and nums[i] == nums[i - 1]: continue

            path.append(nums[i])
            # 这里也不一样 如果不允许重复的话 这里就要使用 i+1 否则使用i
            self.dfs(nums, i + 1, target - nums[i], path, res)
            path.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return
        candidates.sort()

        res = []
        self.dfs(candidates, 0, target, [], res)

        return res


if __name__ == '__main__':
    print(Solution().combinationSum2([2, 3, 6, 7, 7, 1], 8))
