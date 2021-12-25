from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        result = []
        q = deque([root])
        turn = 0
        while len(q) > 0:
            next_q = deque()
            sub_result = []
            while len(q):
                pop = q.popleft()
                if pop != None:
                    next_q.append(pop.left)
                    next_q.append(pop.right)
                    sub_result.append(pop.val)
            if turn == 1:
                sub_result.reverse()
                turn = 0
            else:
                turn = 1
            q = next_q
            if len(sub_result) > 0:
                result.append(sub_result)
        return result
