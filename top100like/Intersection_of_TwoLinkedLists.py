# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
    想法1：
        先扫描一个链表 把每个位置引用添加到set中 再扫描第二个 如果在扫的过程中发现出现在set中 则返回这个引用 否则返回None
    想法2：
        把一把链表反转 然后遍历另一个 如果
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, q = headA, headB

        s = set()

        while p:
            s.add(p)
            p = p.next

        while q:
            if q in s:
                return q
            q = q.next

        return None
