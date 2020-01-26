# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def f(self, root, res):
        if root != None:
            self.f(root.left, res)
            res.append(root.val)
            self.f(root.right, res)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.f(root, res)
        return res
