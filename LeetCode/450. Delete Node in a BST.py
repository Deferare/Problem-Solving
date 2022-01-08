# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def searchMax(root):
            if root == None:
                return None
            elif root.right == None:
                return root
            return searchMax(root.right)
        def delet(root, key):
            if root == None: return None
            if root.val > key:
                root.left = delet(root.left, key)
            elif root.val < key:
                root.right = delet(root.right, key)
            else:
                if root.left == None: return root.right
                elif root.right == None: return root.left
                else:
                    root.val = searchMax(root.left).val
                    root.left = delet(root.left, root.val)
            return root
        result = delet(root, key)
        return result
