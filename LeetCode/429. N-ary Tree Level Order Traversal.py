# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        result = []
        q = deque([root])
        while len(q) > 0:
            q_next = deque()
            result_sub = []
            while len(q) > 0:
                pop = q.popleft()
                if pop != None:
                    result_sub.append(pop.val)
                    for i in range(len(pop.children)):
                        q_next.append(pop.children[i])
            result.append(result_sub)
            q = q_next
        return result
