'''
    这题好像没什么难度 就是基本的数据结构操作
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0

    def get(self, index):
        # print("when get ", self.size)
        if index < 0 or index >= self.size: return -1

        p = self.dummy.next

        while index:
            p = p.next
            index -= 1

        return p.val

    def addAtHead(self, val):

        node = ListNode(val)
        node.next = self.dummy.next
        self.dummy.next = node
        self.size += 1

        # print("add head ", self.size)

    def addAtTail(self, val):
        p = self.dummy
        while p.next:
            p = p.next

        p.next = ListNode(val)
        self.size += 1
        # print("add tail ", self.size)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size: return

        p = self.dummy

        while index:
            p = p.next
            index -= 1

        node = ListNode(val)

        node.next = p.next
        p.next = node
        self.size += 1

        # print("add index ", self.size)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size: return

        p = self.dummy

        while index:
            p = p.next
            index -= 1
        p.next = p.next.next
        self.size -= 1
        # print("dele ", self.size)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
