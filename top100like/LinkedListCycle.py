# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'Node(' + str(self.val) + ')'


class Solution(object):
    '''
        这个方法当然是最愚蠢的 就是用set来保存所有的指针 如果遇到过一次重复的 就return True就行了
        如果没遇到过 就一定会跳出循环 return False
    '''

    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     if not head:
    #         return False
    #
    #     m = set()
    #     while head.next:
    #         if head not in m:
    #             m.add(head)
    #         else:
    #             return True
    #         head = head.next
    #
    #     return False

    '''
        高手代码 就是elegant
        原理就是：如果有环 一个走得快一个走得慢，走得快的在前面 一定能追上慢的一圈
        
        初始：slow 和 fast fast在slow前一个位置，然后slow每次一步 fast每次两步，这样总能追到
        
        这个代码的巧妙还在于它用except来return False 这样就不用判断 slow.next 和 fast.next.next存在了
        
    '''

    # 98.74%  25.53%

    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


if __name__ == '__main__':
    head = ListNode(0)
    node = ListNode(1)

    head.next = node
    node.next = head

    print(head)
    print(head.next)
    print(head.next.next)
    print(Solution().hasCycle(head))
