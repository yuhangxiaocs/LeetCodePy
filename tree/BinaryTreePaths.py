# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path, res = [], []

        def traverse(root, path):
            if not root: return

            if root.left == root.right:
                res.append("->".join(path + [str(root.val)]))
                return

            traverse(root.left, path + [str(root.val)])
            traverse(root.right, path + [str(root.val)])

        traverse(root, path)

        return res
