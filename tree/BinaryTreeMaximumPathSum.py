# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    Use both children, return one
'''


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        self.res = -float('inf')

        # dfs(root)返回值定义为以root为根的最大单条路径

        def dfs(root):
            if not root: return 0

            l = dfs(root.left)
            r = dfs(root.right)

            self.res = max([self.res, root.val + l + r, root.val + l, root.val + r, root.val])

            return max(l, r) + root.val if max(l, r) > 0 else root.val

        dfs(root)
        return self.res

        # 这个形式比较简洁
        def dfs(root):
            if not root: return
            l = max(0, dfs(root.left))
            r = max(0, dfs(root.right))
            self.res = max(self.res, l + r + root.val)
            return max(l, r) + root.val
