# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Floyd cycle detection algorithm
    # tortoise and the hare algorithm
    
    # 51.27% 100.00%
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p = q = head
        try:
            while True:
                p = p.next.next
                q = q.next
                if p == q: break
        except:
            return None

        q = head
        while p != q:
            p = p.next
            q = q.next
        return p
