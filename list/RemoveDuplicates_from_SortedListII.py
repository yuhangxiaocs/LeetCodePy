# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(-float('inf'))
        dummy.next = head

        while cur.next:

            tmp = cur.next

            if tmp.next and tmp.next.val == tmp.val:
                while tmp.next:
                    if tmp.next.val == tmp.val:
                        tmp = tmp.next
                    else:
                        break

                cur.next = tmp.next

            else:
                cur = cur.next

        return dummy.next
