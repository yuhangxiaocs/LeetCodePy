import random
/*
 * 红黑树
 */

RED = True
BLACK = False


class Node:
    def __init__(self, key, color):
        self.key = key
        self.value = 0  # 卫星数据 暂不设置
        self.color = color

        self.left = None
        self.right = None
        self.N = 1


class RBTree:

    def __init__(self):
        self.root = None

    def isRed(self, node):
        # 空节点当做黑色
        if not node: return False
        return node.color == True

    def size(self, root):
        if not root: return 0
        return root.N

    def rotateLeft(self, h):

        x = h.right
        h.right = x.left
        x.left = h

        x.color = h.color
        h.color = RED

        x.N = h.N
        h.N = self.size(h.left) + self.size(h.right) + 1

        return x

    def rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h

        x.color = h.color
        h.color = RED

        x.N = h.N
        h.N = self.size(h.left) + self.size(h.right) + 1
        return x

    def filpColor(self, root):

        root.left.color = BLACK
        root.right.color = BLACK
        # 红链接向上传递
        root.color = RED
        return root

    def _insert(self, root, key):
        if not root: return Node(key, RED)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            # update value 假装更新一下 实际上value并不影响算法
            root.value = 1

        #     以上都是和BST插入相同

        if self.isRed(root.right) and not self.isRed(root.left):
            root = self.rotateLeft(root)

        if self.isRed(root.left) and self.isRed(root.left.left):
            root = self.rotateRight(root)

        if self.isRed(root.left) and self.isRed(root.right):
            root = self.filpColor(root)

        root.N = self.size(root.left) + self.size(root.right) + 1

        return root

    def insert(self, key):
        self.root = self._insert(self.root, key)
        # 确保根节点黑色
        self.root.color = BLACK

    def _show(self, root, d):
        if not root:
            space = "-" * d
            print(space, "null", "d: ", str(d))
            return

        self._show(root.left, d + 1)
        space = "-" * d
        print(space + str(root.N))

        self._show(root.right, d + 1)

    def show(self):
        self._show(self.root, 0)
        

    def search(self,key):
        pass

    def delete(self, key):
        pass

    def deleteMin(self):
        pass

    def deleteMax(self):
        pass


if __name__ == '__main__':
    t = RBTree()

    for i in range(100):
        t.insert(i + 1)

    # print(t.root.left.key)
    # print(t.root.key)
    # print(t.root.right.key)

    # print(t.root.N)
    # print(t.root.left.N)
    # print(t.root.right.N)

    # t.show()
    x = t.root
    dep = 0
    while x:
        dep += 1
        x = x.right
    print(dep)
