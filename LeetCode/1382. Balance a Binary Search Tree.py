# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def pull(root):
            if root == None: return None
            left = pull(root.left)
            if left != None: arr.append(left)
            arr.append(root.val)
            right = pull(root.right)
            if right != None: arr.append(right)

        def createBST(arr):
            if len(arr) == 0: return None
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = createBST(arr[:mid])
            root.right = createBST(arr[mid+1:])
            return root

        arr = []
        pull(root)
        return createBST(arr)
