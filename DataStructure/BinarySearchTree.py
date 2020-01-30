class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinarySearchTree:

    # 二叉搜索树可以作为一个字典 也可以作为一个优先队列

    def __init__(self):
        self.root = None

    def search(self, x):
        node = self.root
        while node:
            if node.val == x:
                return True
            elif x < node.val:
                node = node.left
            else:
                node = node.right
        return False

    def findMin(self):
        node = self.root
        while node.left:
            node = node.left
        return node.val

    def findMax(self):
        node = self.root
        while node.right:
            node = node.right
        return node.val

    def insert(self, x):
        # 处理空树
        if self.root == None:
            self.root = TreeNode(x)
            return
        node = self.root

        # 父节点
        par = None
        # 记录左右
        flag = 1
        while node:
            if x <= node.val:
                par = node
                node = node.left
                flag = 1
            else:
                par = node
                node = node.right
                flag = 2

        node = TreeNode(x)
        if flag == 1:
            par.left = node
        else:
            par.right = node

    # def delete(self):

    # 中序遍历二叉搜索树
    def inorder_tree_walk(self, root):
        if root:
            self.inorder_tree_walk(root.left)
            print(root.val, sep=',')
            self.inorder_tree_walk(root.right)


if __name__ == '__main__':
    t = BinarySearchTree()
    t.insert(7)
    t.insert(6)
    t.insert(9)
    t.insert(8)
    t.inorder_tree_walk(t.root)
    print("min: ", t.findMin())
    print("max: ", t.findMax())
    print('5 in tree:', t.search(5))
    print('6 in tree:', t.search(6))

