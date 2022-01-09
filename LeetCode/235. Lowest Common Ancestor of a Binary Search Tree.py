# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def searchTree(root, check_n):
            if root == None or check_n >= 2:
                return check_n
            if len(result) != 0:
                return check_n
            check_n += searchTree(root.left, 0)
            check_n += searchTree(root.right, 0)
            if root.val == p.val or root.val == q.val:
                check_n += 1
            if check_n == 2:
                result.append(root)
                return check_n
            return check_n
        result = []
        searchTree(root, 0)
        return result[0]
