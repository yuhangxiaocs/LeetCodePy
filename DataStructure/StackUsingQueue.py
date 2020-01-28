from collections import deque


class Stack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        x = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1
        return x

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        x = self.queue1.popleft()

        self.queue2.append(x)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return x

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1


if __name__ == '__main__':
    stack = Stack()

    print(stack.pop())
    for i in range(5):
        stack.push(i)

    for i in range(5):
        print(stack.pop())

    print(stack.pop())
