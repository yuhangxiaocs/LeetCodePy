# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head

        while cur:

            p = cur

            while p.next:
                if p.next.val == cur.val:
                    p.next = p.next.next
                # 这里直接break就可以 因为是sorted array
                else:
                    break

            cur = cur.next

        return head
