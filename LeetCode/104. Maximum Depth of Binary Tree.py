# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def myBfs(node:TreeNode):
    if node == None:
        return 0
    return max(myBfs(node.left), myBfs(node.right)) + 1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return myBfs(root)
