# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        p, q = l1, l2
        carry = 0
        while p or q:

            x = p.val if p else 0
            y = q.val if q else 0

            s = x + y + carry
            carry = s / 10

            cur.next = ListNode(s % 10)

            cur = cur.next
            p = p.next if p else None
            q = q.next if q else None

        if carry > 0:
            cur.next = ListNode(carry)

        return dummy.next

            
