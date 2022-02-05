class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def searchTree(A, B):
            if A == None: return B
            elif B == None: return A
            new = TreeNode(A.val + B.val)
            new.left = searchTree(A.left, B.left)
            new.right = searchTree(A.right, B.right)
            return new
        return searchTree(root1, root2)
