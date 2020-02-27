'''
    delete middle node
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delMiddle(head):
    slow = fast = head
    pre = None
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next

    pre.next = slow.next

    return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    x = delMiddle(head)
    while x:
        print(x.val, end=" ")
        x = x.next
    
