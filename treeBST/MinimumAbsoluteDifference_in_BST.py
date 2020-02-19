# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = []

        def dfs(root, res):
            if not root: return

            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)

        dfs(root, res)
        minV = float('inf')

        for i in range(len(res) - 1):
            minV = min(minV, res[i + 1] - res[i])

        return minV
