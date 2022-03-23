# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        crnt = head
        while crnt != None:
            s += f"{crnt.val}"
            crnt = crnt.next
        return int(s,2)
