# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        crnt_node = headA
        while crnt_node != None:
            s.add(crnt_node)
            crnt_node = crnt_node.next
        crnt_node = headB
        while crnt_node != None:
            if crnt_node in s:
                return crnt_node
            crnt_node = crnt_node.next
        return None
