# Definition for singly-linked list.
'''
    经典好题 使用heap来快速查找最小元素
    使用哑节点dummy来方便处理

'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        if not heap:
            return None

        cur = dummy = ListNode(0)

        while heap:
            node = heapq.heappop(heap)[1]

            cur.next = node

            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            cur = cur.next

        return dummy.next
