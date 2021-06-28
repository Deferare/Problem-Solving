class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = l1; l2 = l2
        if l1 != None:
            crnt = ListNode(l1.val, l1)
        elif l2 != None:
            crnt = ListNode(l2.val, l2)
        else:
            return
        result = crnt
        break_check = 0
        while break_check == 0:
            if l1 == None:
                break_check = 1
                while l2 != None:
                    crnt.next = l2
                    crnt = crnt.next
                    l2 = l2.next
            if l2 == None:
                break_check = 1
                while l1 != None:
                    crnt.next = l1
                    crnt = crnt.next
                    l1 = l1.next
            if break_check == 0:
                if l1.val <= l2.val:
                    crnt.next = l1
                    crnt = crnt.next
                    l1 = l1.next
                else:
                    crnt.next = l2
                    crnt = crnt.next
                    l2 = l2.next
        return result.next
