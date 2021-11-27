# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root != None:
            q = deque([root])
            result.append([root.val])
            while len(q) > 0:
                q_next = deque()
                arr_sub = []
                while len(q) > 0:
                    pop = q.popleft()
                    if pop == None:
                        continue
                    a = pop.left
                    b = pop.right
                    if a != None:
                        q_next.append(a)
                        arr_sub.append(a.val)
                    if b != None:
                        q_next.append(b)
                        arr_sub.append(b.val)
                if len(arr_sub) > 0:
                    result.append(arr_sub)
                q = q_next.copy()
        return result
