# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """



        # 注意这种结构存在大量重叠子问题
        def f(root, can):
            if not root:
                return 0

            if can == True:
                return max(root.val + f(root.left, False) + f(root.right, False), \
                           f(root.left, True) + f(root.right, True))
            else:
                return f(root.left, True) + f(root.right, True)

        return f(root, True)
