# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def f(self, root, res):
        if root != None:
            self.f(root.left, res)
            res.append(root.val)
            self.f(root.right, res)

    # 递归的二叉树中序inorder遍历
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.f(root, res)
        return res

    # 用stack来模拟 先是一直向左走 然后访问跟 然后右子树
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res

            node = stack.pop()
            res.append(node.val)
            # 这一步比较关键
            root = node.right
