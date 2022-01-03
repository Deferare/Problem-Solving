# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root: Node) -> Node:
        head = root
        q = deque([root])
        while len(q) > 0:
            q_next = deque()
            node_crnt = Node()
            while len(q) > 0:
                pop = q.popleft()
                if pop != None:
                    node_crnt.next = pop
                    node_crnt = node_crnt.next
                    if pop.left != None:
                        q_next.append(pop.left)
                    if pop.right != None:
                        q_next.append(pop.right)
            q = q_next.copy()
        return head
