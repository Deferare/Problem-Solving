# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        crnt_node = head
        arr = []
        len_cnt = 0
        while crnt_node != None:
            arr.append(crnt_node.val)
            len_cnt += 1
            crnt_node = crnt_node.next
        for i in range(len_cnt//2):
            if arr[i] != arr[-(i+1)]:
                return False
        return True
