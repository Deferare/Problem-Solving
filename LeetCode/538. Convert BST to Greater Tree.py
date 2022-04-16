# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def convert(root):
            if root == None: return
            convert(root.right)
            crnt_sum[0] += root.val
            root.val = crnt_sum[0]
            convert(root.left)
        crnt_sum = [0]
        convert(root)
        return root
