# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    注意这里说了严格的大于小于关系，不能出现等于
'''


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        res = []

        def dfs(root, res):
            if not root: return

            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)

        dfs(root, res)
        # print(res)

        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]: return False
        return True
