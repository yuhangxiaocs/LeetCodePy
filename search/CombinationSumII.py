class Solution(object):




    def dfs(self, nums, index, target, path, res):
        if target == 0:
            res.append(path[:])  # 注意这里哦 如果不这样拷贝 那就是错了
            return

        for i in range(index, len(nums)):
            # 在这里和在开头剪枝都可以
            if nums[i] > target: break
            path.append(nums[i])
            self.dfs(nums, i, target - nums[i], path, res)
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
    print(Solution().combinationSum([2, 3, 6, 7, 7], 7))
