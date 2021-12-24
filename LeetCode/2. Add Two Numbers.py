class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def extraction(node) -> str:
            if node == None:
                return ""
            return extraction(node.next)+str(node.val)
        def makeListNode(index):
            if index < 0:
                return None
            sub_node = ListNode(int(num[index]))
            sub_node.next = makeListNode(index-1)
            return sub_node
        num = str(int(extraction(l1)) + int(extraction(l2)))
        head = ListNode(int(num[-1]))
        head.next = makeListNode(len(num)-2)
        return head
