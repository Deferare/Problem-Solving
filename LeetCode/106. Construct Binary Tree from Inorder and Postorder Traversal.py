# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        def builder(istart, iend, pstart, pend):
            if istart > iend or pstart > pend:
                return None
            root = TreeNode(postorder[pend])
            iindex = s[root.val]
            root.left = builder(istart, iindex - 1, pstart, pstart + iindex - 1 - istart)
            root.right = builder(iindex + 1, iend, pstart + iindex - istart, pstart - istart + iend - 1)
            return root
        s = dict()
        for i in range(len(inorder)):
            s[inorder[i]] = i
        return builder(0, len(inorder) - 1, 0, len(postorder) - 1)
