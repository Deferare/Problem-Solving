# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root: TreeNode) -> int:
        def recursion(root, state):
            if root == None: return 0
            key = root.__hash__()
            if key in cache and state in cache[key]: return cache[key][state]
            crnt = recursion(root.left, True) + recursion(root.right, True)
            if state:
                crnt =  max(crnt, recursion(root.left, False) + recursion(root.right, False) + root.val)
            if key not in cache: cache[key] = dict()
            cache[key][state] = crnt
            return cache[key][state]
        cache = dict()
        return recursion(root, True)
