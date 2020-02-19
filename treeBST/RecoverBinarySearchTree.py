# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if not root: return
        res = []

        def dfs(root, res):

            if not root: return

            dfs(root.left, res)
            res.append(root)
            dfs(root.right, res)

        dfs(root, res)
        i, j = 0, len(res) - 1

        while i < len(res) and res[i].val <= res[i + 1].val:
            i += 1

        while j >= 0 and res[j - 1].val <= res[j].val:
            j -= 1

        res[i].val, res[j].val = res[j].val, res[i].val
