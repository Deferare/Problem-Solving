# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def myRecursion(start, end):
            nodes = []
            for i in range(start, end + 1):
                for left in myRecursion(start, i - 1):
                    for right in myRecursion(i + 1, end):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        nodes.append(root)
            if len(nodes) == 0:
                return [None]
            return nodes
        result = myRecursion(1, n)
        return result
