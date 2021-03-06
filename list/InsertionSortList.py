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

        last, cur = head, head.next

        while cur:

            # 有序
            if cur.val >= last.val:
                last = cur
                cur = cur.next
                continue

            if cur.next:
                last.next = cur.next
                pre[cur.next] = last
            else:
                last.next = None

            c = p = cur
            cur = cur.next

            while pre[p].val >= c.val:
                p = pre[p]

            #   pre.pre  pre  p

            pre[p].next = c
            c.next = p

            pre[c] = pre[p]
            pre[p] = c

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    x = Solution().insertionSortList(head)

    while x:
        print(x.val, end=" ")
        x = x.next
