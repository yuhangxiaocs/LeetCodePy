# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        p = root
        while p or stack:
            if p:
                res.append(p.val)
                stack.append(p)
                p = p.left

            else:
                node = stack.pop()
                p = node.right
        return res
