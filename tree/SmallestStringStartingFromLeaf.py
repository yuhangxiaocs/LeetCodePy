# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
        分治法是不对的：min root = min(left, right) + root.val
        这是因为，如果left是right的前缀串，这样的话一定是left小，但其实这样是不一定的

        所以就只能老老实实计算路径
    '''

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        ch = chr(ord('a') + root.val)

        if not root.left and not root.right:
            return ch

        l = self.smallestFromLeaf(root.left) + ch
        r = self.smallestFromLeaf(root.right) + ch

        return min(l, r)

    '''
        注意比较一下两种递归，一个有del，一个没有
    '''

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root: return

        def dfs(root, path):
            if not root: return

            ch = chr(ord('a') + root.val)

            if not root.left and not root.right:
                res[0] = min(res[0], "".join(reversed(path + [ch])))

            dfs(root.left, path + [ch])
            dfs(root.right, path + [ch])

        res = [chr(ord('z') + 1)]
        dfs(root, [])
        return res[0]

    '''
        another version of recursion
    '''

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root: return

        def dfs(root, path):
            if not root: return

            ch = chr(ord('a') + root.val)
            path.append(ch)

            if not root.left and not root.right:
                res[0] = min(res[0], "".join(reversed(path)))

            dfs(root.left, path)
            dfs(root.right, path)

            del path[-1]

        res = [chr(ord('z') + 1)]
        dfs(root, [])
        return res[0]
