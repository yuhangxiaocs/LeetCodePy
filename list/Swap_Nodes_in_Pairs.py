# Definition for singly-linked list.

'''
    Given a linked list, swap every two adjacent nodes and return its head.
    You may not modify the values in the list's nodes, only nodes itself may be changed.

    不允许改变值 那就用stack 这里其实不用stack也可以 就用两个变量即可

    递归的方法也比较直观 先该两个 然后递归改后面的
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next: return head

        cur = dummy = ListNode(0)
        stack = [head, head.next]

        while stack:
            n1 = stack.pop()
            n2 = stack.pop() if stack else None

            if n1.next: stack.append(n1.next)
            if n1.next and n1.next.next: stack.append(n1.next.next)

            cur.next = n1
            cur = cur.next

            if n2:
                cur.next = n2
                cur = cur.next
                cur.next = None
            else:
                cur.next = None

        p = dummy.next

        while p:
            print(p.val)
            p = p.next

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)

    Solution().swapPairs(head)
