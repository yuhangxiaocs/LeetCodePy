import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 初始情况
        if not self.minHeap and not self.maxHeap:
            heapq.heappush(self.minHeap, num)
            return

        if self.maxHeap and num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

    # print(len(self.minHeap),len(self.maxHeap))

    def findMedian(self):
        """
        :rtype: float
        """

        while len(self.maxHeap) > len(self.minHeap):
            x = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -x)

        while len(self.maxHeap) < len(self.minHeap):
            x = heapq.heappop(self.minHeap)
            # 大顶堆 用-x
            heapq.heappush(self.maxHeap, -x)

        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]


if __name__ == '__main__':
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    obj.addNum(1)
    print(obj.findMedian())
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(4)
    print(obj.findMedian())
    obj.addNum(5)
    print(obj.findMedian())
