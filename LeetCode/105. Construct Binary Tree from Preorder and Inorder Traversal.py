from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recursion():
            if 0 == len(preorder):
                return None
            pop = preorder.popleft()
            crnt_node = TreeNode(pop)
            index_2 = inor_info[crnt_node.val]
            inorder[index_2] = -5000
            if index_2 > 0 and inorder[index_2 - 1] != -5000 and index_2 < len(inorder) - 1 and inorder[index_2 + 1] != -5000:
                crnt_node.left = recursion()
                crnt_node.right = recursion()
            elif index_2 > 0 and inorder[index_2 - 1] != -5000:
                crnt_node.left = recursion()
            elif index_2 < len(inorder) - 1 and inorder[index_2 + 1] != -5000:
                crnt_node.right = recursion()
            elif index_2 == 0 and inorder[index_2 + 1] != -5000:
                crnt_node.right = recursion()
            elif index_2 == len(inorder) - 1 and inorder[index_2 - 1] != -5000:
                crnt_node.left = recursion()
            return crnt_node
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        preorder = deque(preorder)
        inor_info = dict()
        for i in range(len(inorder)):
            inor_info[inorder[i]] = i
        head = recursion()
        return head
