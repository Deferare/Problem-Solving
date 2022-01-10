# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def searchTree(root):
            if root == None:
                return 1
            left = searchTree(root.left)
            right = searchTree(root.right)
            if left == False or right == False or abs(left - right) > 1: return False
            return max(left, right) + 1
        if not searchTree(root):
            return False
        return True
