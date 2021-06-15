# Definition for singly-linked list.
class ListNode:
    def __init__(self, x = 0):
        self.val = x
        self.next = None
        
class Solution:
    def removeElements(self,head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        while head.val == val:
            if head.next == None:
                head = None
                return head
            head = head.next
        resultHead = head
        while head.next != None:
            if head.next.val == val:
                if head.next.next == None:
                    head.next = None
                    return resultHead
                head.next = head.next.next
            else:
                head = head.next
        return resultHead

        
