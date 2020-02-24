# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


'''
    用stack也可以实现
'''


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def reverse(head):

            if not head.next: return head

            p = reverse(head.next)

            head.next.next = head
            head.next = None

            return p

        l1 = reverse(l1)
        l2 = reverse(l2)

        dummy = cur = ListNode(0)

        s = 0
        while l1 or l2:
            s /= 10
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            s += x + y

            cur.next = ListNode(s % 10)

            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if s / 10: cur.next = ListNode(s / 10)

        return reverse(dummy.next)
