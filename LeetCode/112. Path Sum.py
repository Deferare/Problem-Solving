# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def myRecursive(node, crnt_sum):
            if node == None:
                return False
            crnt_sum += node.val
            if node.left == None and node.right == None:
                if crnt_sum == targetSum:
                    return True
                return False
            if myRecursive(node.left, crnt_sum) or myRecursive(node.right, crnt_sum):
                return True
            return False
        return myRecursive(root, 0)
