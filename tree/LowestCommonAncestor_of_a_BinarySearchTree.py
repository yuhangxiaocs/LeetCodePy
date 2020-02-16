# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        queue = deque([root])

        if p.val > q.val: p, q = q, p

        while queue:

            node = queue.popleft()
            if node.val >= p.val and node.val <= q.val: return node

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
