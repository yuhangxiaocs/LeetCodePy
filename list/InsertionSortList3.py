'''

    这里仿佛有个技巧 如果要在链表中追踪pre 可以显式的使用pre来更新 也可以在每次判断的时候使用pre.next  这样 既有pre 又有pre.next


'''


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

        dummy = ListNode(-float('inf'))
        dummy.next = head

        cur = head
        # 4 2 1 3
        while cur.next:
            print(cur.val)
            tmp = cur.next
            if tmp.val > cur.val:
                cur = cur.next
                continue

            # 由于迭代时 cur  cur.next
            # 所以这里就是改变了 pre指针
            cur.next = tmp.next
            p = dummy

            while p.next.val < tmp.val:
                p = p.next
            tmp.next = p.next
            p.next = tmp

        return dummy.next


'''
        if not head: return
        dummy = ListNode(-float('inf'))
        dummy.next = head
        cur = head
        while cur.next:
            nxt = cur.next
            if nxt.val > cur.val: cur = cur.next; continue
            p = dummy
            cur.next = nxt.next
            while p.next.val < nxt.val: p = p.next
            nxt.next = p.next
            p.next = nxt
        return dummy.next
'''
if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    x = Solution().insertionSortList(head)
    while x:
        print(x.val, end=" ")
        x = x.next
