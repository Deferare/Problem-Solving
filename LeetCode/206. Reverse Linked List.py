# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        arr = []
        crnt_node = head
        while crnt_node != None:
            arr.append(crnt_node)
            crnt_node = crnt_node.next
        head = arr[-1]
        crnt_node = head
        for i in range(len(arr)-1).__reversed__():
            crnt_node.next = arr[i]
            crnt_node = crnt_node.next
        crnt_node.next = None
        return head
