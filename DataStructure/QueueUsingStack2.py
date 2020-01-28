class Queue:

    # 这是一种思路 也比较好像
    # 还有一种思路 更快一点 在pop的时候是秒取
    # 就是push的时候始终push到stack1，然后pop的时候始终从stack2取
    # 如果stack2是空 则将stack1加进去就行 我靠 这个更妙啊
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        # 记录最下面的元素
        self.front = None

    def enqueue(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def dequeue(self):

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # [-1]就是peek
        if self.stack2:
            return self.stack2[-1]
        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # 此时两个stack的元素都是queue中的元素
        # 第一种方法中的stack2只是一个中转 所有的元素都在stack1中
        return (not self.stack1) and (not self.stack2)


if __name__ == '__main__':
    queue = Queue()
    print(queue.dequeue())

    for i in range(5):
        queue.enqueue(i)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
