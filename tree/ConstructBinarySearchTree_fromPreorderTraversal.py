# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
    Runtime: 20 ms, faster than 90.75% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.
    Memory Usage: 11.9 MB, less than 85.71% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.
'''


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return None

        rootVal = preorder[0]

        i = 1
        while i < len(preorder):
            if preorder[i] > rootVal: break
            i += 1

        root = TreeNode(rootVal)

        root.left = self.bstFromPreorder(preorder[1:i])

        root.right = self.bstFromPreorder(preorder[i:])

        return root
