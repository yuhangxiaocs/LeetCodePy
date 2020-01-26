# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self):
        self.head = None

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        curr = head

        while curr != None:
            t = curr
            curr = curr.next
            t.next = last
            last = t

        return last

    # 递归法反转 每次递归回来的时候 其实返回的都是一个表头
    # 而操作都是当前操作的 因为递归可以记住并保存所有状态
    # 因而在每一次都可以用head.next.next = head 这种操作
    # 而不担心被覆盖

    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp
