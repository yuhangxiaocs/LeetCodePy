# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


'''
    线性时间 O1内存
    把值加到l1上面，用一个pre指针追踪它前面的一个
    
    另外这里的进位处理 不是常用的显式carry 而是都加到一起 每次进入循环的时候得到进位 原理是一样的
'''


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p, q = l1, l2
        # add to p
        pre_p, s = None, 0
        while p and q:
            s //= 10  # get the carry
            s += p.val + q.val
            p.val = s % 10
            pre_p, p, q = p, p.next, q.next

        if q:
            pre_p.next = q
            p = q

        while p:
            s //= 10
            s += p.val
            p.val = s % 10
            pre_p, p = p, p.next

        if s // 10: pre_p.next = ListNode(s // 10)

        return l1


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = Solution().addTwoNumbers(l1, l2)

    while res:
        print(res.val, end=' ')
        res = res.next
