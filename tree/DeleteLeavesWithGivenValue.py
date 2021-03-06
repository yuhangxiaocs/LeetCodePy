# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    1325. Delete Leaves With a Given Value

    Given a binary tree root and an integer target, delete all the leaf nodes with value target.

    Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node
    and has the value target, it should also be deleted (you need to continue doing that until you can't).


    Runtime: 40 ms, faster than 87.25% of Python online submissions for Delete Leaves With a Given Value.
    Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Delete Leaves With a Given Value.
'''


class Solution(object):
    '''
        简化版本，先处理左右孩子，再处理本身，下面的复杂的写法，也不能算错，只是略显荣誉，但是可以起到剪枝作用
    '''

    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root: return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # root.left == root.right也就是都为空
        if root.left == root.right and root.val == target:
            return None
        else:
            return root

    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root: return None

        if not root.left and not root.right:
            if root.val == target:
                return None
            else:
                return root

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # 既然上面做了改动，那么这里就有可能变成叶节点
        if not root.left and not root.right:
            if root.val == target:
                return None
            else:
                return root

        return root
