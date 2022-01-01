# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode):
        def myRecursive(node):
            if node == None:
                return
            result.append(node.val)
            myRecursive(node.left)
            myRecursive(node.right)
        result = []
        myRecursive(root)
        return result
