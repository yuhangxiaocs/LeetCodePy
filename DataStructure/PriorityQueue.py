class PriorityQueue:

    def __init__(self, capaticy):
        self.capacity = capaticy
        self.size = 0
        self.nums = [] * (capaticy + 1)
        # 如果是大顶堆 最开始的就设置为最大值 反之设置为最小的
        self.nums[0] = 999999

    # 大顶堆
    def insert(self, x):
        self.size += 1
        pos = self.size
        while x > self.nums[pos / 2]:
            self.nums[pos] = self.nums[pos / 2]
            pos /= 2
        self.nums[pos] = x

    def delete(self):
        if self.size < 1:
            return 'error'

        x = self.nums[1]
        self.nums[1] = self.nums[self.size]

        pos = 1
        while self.nums[pos * 2] > self.nums[self.size]:
            self.nums[pos] = self.nums[pos * 2]
            pos *= 2
        self.nums[pos] = self.nums[self.size]
        self.size -= 1
        return x

    def __len__(self):
        return self.size
