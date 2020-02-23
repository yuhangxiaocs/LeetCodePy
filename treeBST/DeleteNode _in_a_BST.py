# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    删除BST的节点分如下几种情况：
    1. 要删除的节点没有左右孩子，那么直接删除即可
    2. 要删除的节点只有一个子分支，那么用这个分支替代当前的root即可
    3. 待删除的节点左右孩子都有，那么用右子树中最小的元素替代root，并将那个最小的删除

    下面的分类做了一些改变
    if not root.right:
    既包含了root.left存在you包含了它不存在的情况
    if not root.left 同理
    最后就剩下都存在的情况
'''


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)


        else:
            if not root.left: return root.right
            if not root.right: return root.left

            # have both subtree
            # 用右子树的最小值代替root并删除最小值节点
            tmp = root.right
            minV = tmp.val

            while tmp.left:
                tmp = tmp.left
                minV = tmp.val

            root.val = minV

            root.right = self.deleteNode(root.right, root.val)

        return root
