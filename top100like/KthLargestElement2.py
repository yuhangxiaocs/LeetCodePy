import heapq


class Solution(object):

    # 92.50% 100.00%
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:k]

        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
