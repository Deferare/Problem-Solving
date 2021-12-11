class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def recursion(node):
            if node == None:
                return None
            elif node.next == None:
                return node
            nx = node.next
            node.next = recursion(nx.next)
            nx.next = node
            return nx
        result_head = recursion(head)
        return result_head
