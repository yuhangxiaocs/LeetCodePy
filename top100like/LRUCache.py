class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.pre = None
        self.next = None


#  94.36% 55.56%
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        # map存储key --> 链表地址
        self.map = {}
        # 双端链表
        self.head = Node(0, 0)
        # 记录尾指针
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
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            node = self.map[key]
            v = node.value
            self.delete(node)
            self.appendLeft(node)
            return v
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            node = self.map[key]
            self.delete(node)
            newNode = Node(key, value)
            self.map[key] = newNode
            self.appendLeft(newNode)
        else:
            # 如果有容量
            if self.size < self.capacity:
                self.size += 1
                node = Node(key, value)
                self.map[key] = node
                self.appendLeft(node)
            else:
                # 没容量就删除为节点
                tail = self.tail.pre
                self.delete(tail)
                del self.map[tail.key]

                node = Node(key, value)
                self.appendLeft(node)
                self.map[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    obj = LRUCache(2)
    print(obj.map)

    obj.put(1, 1)
    print(obj.size)

    obj.put(2, 2)
    obj.put(3, 3)
    print(obj.map)
