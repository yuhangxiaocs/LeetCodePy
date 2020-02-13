# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = deque()
        q.append([1, root])

        while q:
            x = len(q)
            while x:
                d, node = q.popleft()
                if not node.left and not node.right: return d

                if node.left: q.append([d + 1, node.left])
                if node.right: q.append([d + 1, node.right])
                x -= 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return (l + r + 1) if (not l or not r) else min(l, r) + 1
