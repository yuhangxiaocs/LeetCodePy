'''
    这个要求栈能返回最小元素，当然用堆是可以实现的，但是代价太大；
    用一个元素保存当前最小的，也不行，因为一旦元素出栈，还要去修改那个min，而且不好修改

    从第二个思路改进，不放多用些内存来换取时间，对于每个元素，都将它进入stack时的最小值和它一起
    作为一个元组存进stack中，这样就可以一下取出了

    启发：不要盲目用数据结构，先找问题所在，然后先从最朴素的方法开始想去，缺什么用什么，没必要为了算法而算法
'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x, curMin))

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None

        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
