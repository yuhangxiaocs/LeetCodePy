# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
    这个想法是这样的 a都到头了 就从b的头开始走 b走到头的就从a的头开始走 这样两种走的长度都是

    A     *****
              *******
    B**********
    假设A长度为 s+k
    假设B长度为 m+k

    按这种策略走到交汇点 A走了s+m+k
                      B走了s+m+k

    若没有交汇点 最终也会都是None 因为走的长度都是一样的=两个长度之和

    这谁能想到啊...
'''


class Solution(object):
    # 98.76% 22.67%
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
