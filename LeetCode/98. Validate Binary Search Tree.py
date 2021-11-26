# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def myRecursion(node: TreeNode, _min, _max):
    if node == None:
        return True
    if _min != None and node.val <= _min:
        return False
    if _max != None and node.val >= _max:
        return False
    if myRecursion(node.left, _min, node.val) and myRecursion(node.right, node.val, _max):
        return True
    return False
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return myRecursion(root, None, None)
