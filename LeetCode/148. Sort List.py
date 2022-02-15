# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None: return None
        elif head.next == None: return head

        if head.val <= head.next.val:
            left = ListNode(head.val)
            right = ListNode(head.next.val)
        else:
            left = ListNode(head.next.val)
            right = ListNode(head.val)
        left.next = right
        mid = left
        crnt = head.next.next

        while crnt != None:
            new = ListNode(crnt.val)
            if new.val <= left.val:
                new.next = left
                left = new
            elif new.val >= right.val:
                right.next = new
                right = new
                mid = left.next
            else:
                if crnt.val > mid.val: sub = mid
                else: sub = left
                while True:
                    if sub.next.val >= new.val:
                        new.next = sub.next
                        sub.next = new
                        mid = new
                        break
                    sub = sub.next
            crnt = crnt.next
        return left
