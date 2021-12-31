# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = dict()
        index = 0
        crnt_Node = head
        while crnt_Node != None:
            hash_crnt = crnt_Node.__hash__()
            if hash_crnt in d:
                return d[hash_crnt]
            d[hash_crnt] = crnt_Node
            crnt_Node = crnt_Node.next
            index += 1
        return None
