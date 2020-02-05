# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 要加判断非空
        if not head or head.next == None:
            return head

        # slow每次一步 fast每次两步
        pre = slow = fast = head

        # 分成两段以head开头和slow开头
        while slow and fast:
            pre = slow
            slow = slow.next
            # 防止空指针
            if fast.next:
                fast = fast.next.next
            else:
                break
            # 断链
        pre.next = None

        # 加了这个赋值就对了
        head = self.sortList(head)
        slow = self.sortList(slow)

        def mergeTwoLists(l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            head = cur = ListNode(0)

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2

            return head.next

        return mergeTwoLists(head, slow)


if __name__ == '__main__':
    head = ListNode(4)
    node1 = ListNode(2)
    node2 = ListNode(1)
    node3 = ListNode(3)

    head.next = node1
    node1.next = node2
    node2.next = node3

    p = head
    while p:
        print(p.val, end=" ")
        p = p.next

    res = Solution().sortList(head)
    print()
    while res:
        print(res.val, end=' ')
        res = res.next
