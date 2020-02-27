# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.root = None

        def convert(head, root):
            if not head: return None
            if not head.next: return TreeNode(head.val)

            slow = fast = head
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next

            pre.next = None

            root = TreeNode(slow.val)

            root.left = convert(head, root.left)
            root.right = convert(slow.next, root.right)

            return root

        self.root = convert(head, self.root)

        return self.root


'''
    a slightly different version
'''


def sortedListToBST(self, head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    self.root = None

    if not head: return
    if not head.next: return TreeNode(head.val)

    slow = fast = head
    pre = None
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next

    pre.next = None

    root = TreeNode(slow.val)

    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(slow.next)

    return root
