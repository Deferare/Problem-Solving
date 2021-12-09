# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def recursion(node):
            if node == None:
                return
            stack.append(node)
            if node.left != None:
                recursion(node.left)
            elif node.right == None:
                while len(stack) != 0:
                    pop = stack.pop()
                    result.append(pop.val)
                    recursion(pop.right)
            else:
                while len(stack) != 0:
                    pop = stack.pop()
                    result.append(pop.val)
                    recursion(pop.right)
        result = []
        stack = deque()
        recursion(root)
        return result
