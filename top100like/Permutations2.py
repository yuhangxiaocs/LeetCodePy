class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        path, res = [], []
        self.dfs(nums, path, res)
        # print(res)

        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        # 就是每次取一个元素 然后剩余的依然按照原顺序
        # 我的方法之所以要用used数组 就是为了防止重复使用
        # 而这里 直接将用过的删除了 就很好了
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
