import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


'''
    如下问题：
        head0--node--node--node--node--
        head1--node--node--node--node--node--
        head2--node--node--node--node--
        head3--node--node--node--node--node--node--
    归并若干个有序链表
    
    第一个元素一定是在所有的head里面选一个，因为head是每链里最小的
    所以只要快速将最小的选出来就可以了，这样的话就想到了了heap结构
    此外，添加的时候，将(val, node)同时添加，python中某人第一个为权值
    这样一来就可以快速找到链
    
    每次找到最小的添加进去以后，这个位置的指针就要向后移动一个
'''


class Solution(object):
    # 84.40% 28.79%
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # edge case
        if not lists:
            return None

        heap = []
        # 将所有非空的节点先添加到堆中，
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        # 防止[ [] ]情况
        if not heap:
            return None
        # 头结点等于第一个取出来的
        head = heapq.heappop(heap)[1]
        # 每次插入之前都要判断是否存在，确保在heap中的都是非空的
        if head.next:
            heapq.heappush(heap, (head.next.val, head.next))
        # 用p作为迭代变量
        p = head
        while heap:
            node = heapq.heappop(heap)[1]
            p.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            p = p.next

        return head


'''
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
'''
