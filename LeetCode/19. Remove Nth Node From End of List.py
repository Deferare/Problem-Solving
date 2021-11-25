# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        len_cnt = 0
        crnt_node = head
        while crnt_node != None:
            crnt_node = crnt_node.next
            len_cnt += 1
        if len_cnt == n:
            head = head.next
            return head
        index = 0
        crnt_node = head
        while crnt_node.next != None:
            if index < len_cnt-n-1:
                crnt_node = crnt_node.next
                index += 1
            else:
                crnt_node.next = crnt_node.next.next
                break
        return head
