class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int):
        if head == None or k == 0:
            return head
        def nodeCnt(node):
            if node == None:
                return 0
            arr.append(node)
            return nodeCnt(node.next) + 1
        arr = []
        nodeList_n = nodeCnt(head)
        if nodeList_n <= k:
            k = k%nodeList_n
        if k == 0:
            return head
        head = arr[-k]
        crnt_node = head
        for i in range(nodeList_n-k+1, nodeList_n):
            crnt_node.next = arr[i]
            crnt_node = crnt_node.next
        for i in range(nodeList_n-k):
            crnt_node.next = arr[i]
            crnt_node = crnt_node.next
        crnt_node.next = None
        return head
