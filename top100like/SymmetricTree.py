# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    Runtime: 16 ms, faster than 93.62% of Python online submissions for Symmetric Tree.
    Memory Usage: 12 MB, less than 65.22% of Python online submissions for Symmetric Tree.
    '''

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, l, r):
        if not l and not r:
            return True
        if l and r:
            if l.val != r.val:
                return False
            return self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)

        return False
