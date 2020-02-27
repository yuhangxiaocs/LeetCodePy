'''
    remove duplicates from an unsorted linked list
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeDups(head):
    cur = head

    while cur:

        p = cur

        while p.next:
            if p.next.val == cur.val:
                p.next = p.next.next
            else:
                p = p.next

        cur = cur.next

    return head


if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)

    p = removeDups(head)

    while p:
        print(p.val, end=" ")
        p = p.next
