# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def searchTree(root):
            if root == None: return 0
            left = searchTree(root.left)
            right = searchTree(root.right)
            call_back = max(left, right)
            result[0] = max(result[0], left + right)
            return call_back + 1
        result = [0]
        searchTree(root)
        return result[0]
