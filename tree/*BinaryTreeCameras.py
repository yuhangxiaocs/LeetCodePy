# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC++Python-Greedy-DFS


    思路非常清晰，简单。但是花了好一会本弱鸡才把代码捋清😭，按照下面的逻辑把代码写了出来。
    2---孤儿，不需要父母照顾
    1---爸爸，可以照顾儿子和父母
    0---啃老族：爸爸带带我。

    两个后继都是孤儿时（2），不需要干任何事，可以化身啃老族（0）。
    当你的后继里面有啃老族（0），你就必须成为爸爸（1）-----camera+1
    当你的后继里面有爸爸（1）时，你又变成里不需要任何照顾的孤儿（2）。

    def minCameraCover(self, root):
        self.res = 0
        def dfs(root):
            if not root:
                return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == r == 2: #后继都是孤儿
                return 0    #成为啃老族
            if l == 0 or r == 0:    #后继里有啃老族
                self.res += 1
                return 1    #成为爸爸
            if l == 1 or r == 1:    #后继里有爸爸
                return 2    #成为不用任何照顾的孤儿
        return int(dfs(root) == 0) + self.res
'''


class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        # 2 covered
        # 1 need camera
        # 0 other
        def dfs(root):

            if not root: return 2

            l = dfs(root.left)
            r = dfs(root.right)

            if l == 2 and r == 2: return 0

            if l == 0 or r == 0:
                self.res += 1
                return 1

            if l == 1 or r == 1:
                return 2

        return int(dfs(root) == 0) + self.res
