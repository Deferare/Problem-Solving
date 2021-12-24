# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        def recursion(node):
            if node == None:
                return None
            elif node.next == None:
                return node
            sub_node = ListNode(node.val)
            sub_node.next = recursion(node.next.next)
            return sub_node
        def endNode(node):
            if node == None:
                return None
            elif node.next == None:
                return node
            return endNode(node.next)
        if head == None:
            return None
        a = recursion(head)
        if head.next != None:
            b = recursion(head.next)
            endNode(a).next = b
        return a
