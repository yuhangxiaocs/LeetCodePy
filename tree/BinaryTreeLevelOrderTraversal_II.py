# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return

        res = []
        q = deque()
        q.append([1, root])

        while q:
            level, node = q.popleft()
            if level <= len(res):
                res[level - 1].append(node.val)
            else:
                res.append([node.val])

            if node.left: q.append([level + 1, node.left])
            if node.right: q.append([level + 1, node.right])

        return reversed(res)
