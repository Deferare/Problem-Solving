# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def recursion(node_1, node_2):
            if node_1 == None and node_2 == None:
                return True
            elif node_1 == None or node_2 == None:
                return False
            if node_1.val != node_2.val:
                return False
            if recursion(node_1.left, node_2.left) and recursion(node_1.right, node_2.right):
                return True
            return False
        return recursion(p, q)
