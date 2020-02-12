"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return None

        q = deque([root])
        res = []

        while q:
            tmp = []
            x = len(q)
            while x:
                node = q.popleft()
                tmp.append(node.val)
                x -= 1
                for child in node.children:
                    if child:
                        q.append(child)

            if tmp:
                res.append(tmp[:])

        return res
