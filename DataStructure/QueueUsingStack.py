class Queue:

    # 这是一种思路 也比较好像
    # 还有一种思路 更快一点 在pop的时候是秒取
    # 就是push的时候始终push到stack1，然后pop的时候始终从stack2取
    # 如果stack2是空 则将stack1加进去就行 我靠 这个更妙啊
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack1:
            return "error"
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        x = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return x

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack1:
            return self.stack1[0]
        return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1


if __name__ == '__main__':
    queue = Queue()
    print(queue.dequeue())

    for i in range(5):
        queue.enqueue(i)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    a = []
    a.append(1)
    a.append(2)
    a.append(3)
    print(a)
    print(a[0])
