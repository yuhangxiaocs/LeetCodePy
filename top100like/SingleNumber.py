class Solution(object):
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
