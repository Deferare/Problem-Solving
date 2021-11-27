# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q_main = deque([root])
        while len(q_main) > 0:
            q_next = deque()
            while len(q_main) > 0:
                pop = q_main.popleft()
                if pop != None:
                    if pop.left == None:
                        q_next.append(None)
                    else:
                        q_next.append(pop.left)
                    if pop.right == None:
                        q_next.append(None)
                    else:
                        q_next.append(pop.right)
            q_main = q_next.copy()
            for i in range(len(q_next)//2):
                if q_next[i] == None and q_next[-(i+1)] == None:
                    continue
                elif q_next[i] == None or q_next[-(i+1)] == None:
                    return False
                elif q_next[i].val != q_next[-(i+1)].val:
                    return False
        return True
