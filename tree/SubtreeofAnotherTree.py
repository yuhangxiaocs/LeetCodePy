# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def contains(self, s, t):
        if not t and not s: return True
        if not t or not s: return False

        if s.val != t.val: return False

        l = self.contains(s.left, t.left)
        r = self.contains(s.right, t.right)

        return l and r

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s: return False

        stack = [s]

        while stack:
            node = stack.pop()
            if self.contains(node, t) == True:
                return True
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        return False

