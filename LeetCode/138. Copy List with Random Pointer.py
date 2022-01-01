"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def myCopy(node_or, node_cp):
            if node_or == None:
                return None
            else:
                hash_v = node_or.__hash__()
                if hash_v in visited:
                    return visited[hash_v]
                visited[hash_v] = node_cp
            node_cp.val = node_or.val
            next_cp = Node(node_or.val)
            next_cp = myCopy(node_or.next, next_cp)
            node_cp.next = next_cp
            random_cp = Node(node_or.val)
            random_cp = myCopy(node_or.random, random_cp)
            node_cp.random = random_cp
            return node_cp

        if head == None:
            return None
        visited = dict()
        head_cp = Node(head.val)
        head_cp = myCopy(head, head_cp)
        return head_cp
