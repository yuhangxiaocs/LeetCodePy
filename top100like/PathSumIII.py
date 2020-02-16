# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    思路是这样的，一个dic用于保存当前路径上的前缀和，注意是当前路劲，比如一条路劲是1，2，3那么前缀和分别是0，1，3，6注意有个0在前面；
    比如我们要求的和是2，如果存在的话，那一定是两个前缀和相减，就想快速算出区间和的那道题一样，反之如果某个前缀和减去目标和，如果得到
    的结果在前缀和中，一样也可以说明有这样一个和，那么如何快速找到在不在呢，这就很自然的想到hashmap，所以hashmap用于存储当前路径上每个前缀和
    对应的数目，因为不止有一种，否则我们用集合存储前缀和就可以了，

    为什么强调是当前路径呢，因为不同的路径可能会有重合，所以最后一行的那个-1就是为了到其他路径时避免计算重复，这个方法很巧妙，将值存在map中，
    省去了很多不必要的计算，一次易错的地方是{0:1}的添加，如果不加这个就会少了从root出发的路径，造成漏算；


'''
class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        dic = {0: 1}
        self.count = 0

        def helper(root, curSum, target):
            if not root: return

            curSum += root.val

            if curSum - target in dic:
                # dic[curSum - target]
                # 这里是关键
                self.count += dic[curSum - target]

            if curSum in dic:
                dic[curSum] += 1
            else:
                dic[curSum] = 1

            helper(root.left, curSum, target)
            helper(root.right, curSum, target)

            dic[curSum] -= 1
        # 一旦上面递归结束，就意味着当前点不再是路径上的点了，所以由它产生的路径和要-1
        helper(root, 0, sum)

        return self.count
