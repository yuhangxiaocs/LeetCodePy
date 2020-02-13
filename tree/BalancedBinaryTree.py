# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        flag = [True]

        def dv(root):
            if not root: return 0

            l = dv(root.left)
            r = dv(root.right)

            if abs(l - r) > 1:
                flag[0] = False

            return max(l, r) + 1

        dv(root)

        return flag[0]
