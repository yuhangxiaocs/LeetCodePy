import heapq
import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), count.get)


if __name__ == '__main__':
    a = [1, 2, 3, 2, 4, 4, 4, 4, 5, 5, 5]
    count = collections.Counter(a)
    print(count)
    print(count.get)
    res = heapq.nlargest(3, count.keys(), key=count.get)
    print(res)
