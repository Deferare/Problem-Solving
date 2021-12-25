from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        q = deque([root])
        while len(q) > 0:
            next_q = deque()
            crnt_node = Node()
            while len(q) > 0:
                pop = q.popleft()
                if pop != None:
                    next_q.append(pop.left)
                    next_q.append(pop.right)
                    crnt_node.next = pop
                    crnt_node = crnt_node.next
            q = next_q
        return root
