class Solution(object):

    # 使用字典dict求解
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] = a[i] + 1
        for k, v in a.iteritems():
            if v == 1:
                return k

    # 利用求和
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


    # 利用异或操作的性质 妙
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i

        return a
