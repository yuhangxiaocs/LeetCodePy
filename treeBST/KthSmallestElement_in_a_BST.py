# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: return
        res = []

        def dfs(root, res):
            if not root: return

            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)

        dfs(root, res)

        return res[k - 1]
