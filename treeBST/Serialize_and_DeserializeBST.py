'''
    序列化BST 就是和重建那个是一样的，首先要想，怎么样重建成一样的，只要得到一个preorder或者 postorder即可

    注意python 2.x的split是没有关键字参数的

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root: return ""
        res = []

        def preOrder(root):
            if not root: return

            res.append(str(root.val))
            res.append(',')

            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        res.pop()

        return "".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        # 注意python 2.x的split是没有关键字参数的
        data = list(map(int, data.split(sep=',')))

        def dfs(data):

            if not data: return None

            val = data[0]

            pos = 0
            while pos < len(data) and data[pos] <= val:
                pos += 1

            root = TreeNode(data[0])

            root.left = dfs(data[1:pos])

            root.right = dfs(data[pos:])

            return root

        return dfs(data)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    root = TreeNode(50)
    root.left = TreeNode(40)
    root.right = TreeNode(60)

    obj = Codec()

    string = obj.serialize(root)
    res = obj.deserialize(string)
    print(string)

    print(res)
    print(res.val, res.left.val, res.right.val)
