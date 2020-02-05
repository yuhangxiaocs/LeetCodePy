class Solution:
    def subsets(self, nums):
        # 67.74% 100.00%
        def sub(nums, index, path, res):
            if index == len(nums):
                res.append(path)
                return
            # 不取
            sub(nums, index + 1, path, res)
            # 取
            sub(nums, index + 1, path + [nums[index]], res)

        res = []

        sub(nums, 0, [], res)

        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
