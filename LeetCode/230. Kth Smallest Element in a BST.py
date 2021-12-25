# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def recursion(node):
            if len(arr) == k:
                return arr[-1]
            if node == None:
                return None
            elif node.left != None:
                s = recursion(node.left)
                if s != None:
                    return s
                arr.append(node.val)
                s = recursion(node.right)
                if s != None:
                    return s
            elif node.right != None:
                arr.append(node.val)
                s = recursion(node.right)
                if s != None:
                    return s
            else:
                arr.append(node.val)
                if len(arr) == k:
                    return arr[-1]
        arr = []
        return recursion(root)
