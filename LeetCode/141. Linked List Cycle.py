# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        crnt_node = head
        s = set()
        while crnt_node != None:
            if crnt_node in s:
                return True
            else:
                s.add(crnt_node)
                crnt_node = crnt_node.next
        return False
