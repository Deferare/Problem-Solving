# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def myBFS(root, depth):
            if root == None: return None
            depth += 1
            left = myBFS(root.left, depth)
            right = myBFS(root.right, depth)
            if left != None and right != None:
                if left[1] > right[1]: return left
                elif left[1] < right[1]: return right
                else: return [left[0]+right[0], right[1]]
            elif left != None: return left
            elif right != None: return right
            return [root.val, depth]
        return myBFS(root, 0)[0]
