# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head

        pre = {}
        dummy = ListNode(-float('inf'))
        dummy.next = head

        last, cur = dummy, head
        while cur:
            pre[cur] = last
            last = cur
            cur = cur.next

        cur = head.next

        while cur:

            val = cur.val

            p = cur
            cur = cur.next

            while pre[p].val > val:
                p.val = pre[p].val
                p = pre[p]

            p.val = val

        return dummy.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    x = Solution().insertionSortList(head)

    while x:
        print(x.val, end=" ")
        x = x.next
