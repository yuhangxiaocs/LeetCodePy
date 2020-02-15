# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        res1, res2 = [], []

        def inOrder(root, res):
            if not root: return

            if not root.left and not root.right:
                res.append(root.val)

            inOrder(root.left, res)
            inOrder(root.right, res)

        inOrder(root1, res1)
        inOrder(root2, res2)
        # print(res1)
        # print(res2)

        for a, b in zip(res1, res2):
            if a != b: return False

        return res1 and res2
