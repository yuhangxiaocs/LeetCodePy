# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
    不用额外空间的方法 反转一半链表
    https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space
'''


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        ans = []
        p = head
        while p:
            ans.append(p.val)
            p = p.next

        i, j = 0, len(ans) - 1
        while i <= j:
            if ans[i] != ans[j]:
                return False
            i += 1
            j -= 1
        return True
