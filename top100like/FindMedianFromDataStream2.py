import heapq


class MedianFinder:

    '''
        先往maxHeap插入 然后 将其中最大的 放到minHeap
    '''
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
        heapq.heappush(self.maxHeap, -num)

        x = heapq.heappop(self.maxHeap)

        heapq.heappush(self.minHeap, -x)

        if len(self.maxHeap) < len(self.minHeap):
            x = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -x)

    # print(len(self.minHeap),len(self.maxHeap))

    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    print(obj.findMedian())
    obj.addNum(2)
    print(obj.findMedian())
