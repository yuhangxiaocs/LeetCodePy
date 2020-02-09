class Solution(object):
    '''
        It turns out we can do it in one-pass.
        While we iterate and inserting elements into the table, we also
        look back to check if current element's complement already exists
        in the table. If it exists, we have found a solution and return immediately.
    '''

    # 99.73%  20%
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                res = [dic[target - nums[i]], i]
                res.sort()
                return res
            # 要后做这一步 为了防止 重复元素 [3, 3] 6
            dic[nums[i]] = i


if __name__ == '__main__':
    print(Solution().twoSum([3, 3], 6))
