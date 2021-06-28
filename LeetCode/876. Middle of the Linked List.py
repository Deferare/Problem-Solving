class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        first_crnt = head
        second_crnt = head
        step_check = 2
        while first_crnt.next != None:
            first_crnt = first_crnt.next
            if step_check%2 == 0:
                second_crnt = second_crnt.next
            step_check += 1
        return second_crnt
