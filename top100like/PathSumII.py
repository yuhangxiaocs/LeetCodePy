# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findPath(self, root, sum, path, res):
        if not root:
            return

        if not root.left and not root.right and sum - root.val == 0:
            res.append(path + [root.val])

        return self.findPath(root.left, sum - root.val, path + [root.val], res) or \
               self.findPath(root.right, sum - root.val, path + [root.val], res)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path, res = [], []
        self.findPath(root, sum, path, res)
        return res

    # *******************

    # 将上面两个合并到一个函数：
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path, res = [], []

        def findPath(root, sum, path, res):
            if not root:
                return

            if not root.left and not root.right and sum - root.val == 0:
                res.append(path + [root.val])

            return findPath(root.left, sum - root.val, path + [root.val], res) or \
                   findPath(root.right, sum - root.val, path + [root.val], res)

        findPath(root, sum, path, res)
        return res
