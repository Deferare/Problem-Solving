class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def recursion(node):
            if node == None:
                return None
            if val == node.val:
                return node
            elif val < node.val:
                return recursion(node.left)
            else:
                return recursion(node.right)
        result = recursion(root)
        return result
