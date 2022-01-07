# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def depthSearch(root):
            if root == None:
                return 0
            max_check = 0
            for i in range(len(root.children)):
                crnt = depthSearch(root.children[i])
                if crnt > max_check:
                    max_check = crnt
            return max_check + 1
        result = depthSearch(root)
        return result
