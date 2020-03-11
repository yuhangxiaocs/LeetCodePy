'''

'''


class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.pre = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    # 删除元素
    def delete(self, node):
        p = node.pre
        q = node.next
        p.next = q
        q.pre = p

    # 插入到头部
    def appendLeft(self, node):
        first = self.head.next
        node.next = first
        first.pre = node
        node.pre = self.head
        self.head.next = node

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.delete(node)
            self.appendLeft(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.dic:
            self.delete(self.dic[key])

        node = Node(key, value)
        self.appendLeft(node)
        self.dic[key] = node

        if len(self.dic) > self.capacity:
            # 这两行顺序不能错
            del self.dic[self.tail.pre.key]
            self.delete(self.tail.pre)


if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(1)
    obj.put(2, 1)
    obj.get(2)
    print(obj.head.next.key)
    obj.put(3, 2)

    # obj.get(2)

    # obj.put(2, 2)
    # obj.get(1)
    # print(obj.tail.pre.value)

    # obj.put(3, 3)
    # obj.get(2)

    # obj.put(4, 4)
