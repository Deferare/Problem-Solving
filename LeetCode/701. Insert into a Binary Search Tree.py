# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root:TreeNode, val: int) -> TreeNode:
        if root == None: return TreeNode(val)
        def recursion(root):
            if root == None:
                return None
            if root.val < val:
                if root.right == None:
                    root.right = TreeNode(val)
                else:
                    recursion(root.right)
            elif root.val > val:
                if root.left == None:
                    root.left = TreeNode(val)
                else:
                    recursion(root.left)
        recursion(root)
        return root
