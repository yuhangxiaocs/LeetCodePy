# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
注意是从root到leaf的路径
'''


class Solution(object):

    def traverse(self, root, curSum, sum, res):
        if not root:
            return

        if not root.left and not root.right and curSum + root.val == sum:
            res.append('yes')
            return

        self.traverse(root.left, curSum + root.val, sum, res)
        self.traverse(root.right, curSum + root.val, sum, res)

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []

        if not root:
            return False

        self.traverse(root, 0, sum, res)

        return res
