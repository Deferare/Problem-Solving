# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    pointer = -1
    def __init__(self, root: TreeNode):
        self.arr = []
        def recursion(root):
            if root == None:
                return
            recursion(root.left)
            self.arr.append(root.val)
            recursion(root.right)
        recursion(root)
    def next(self) -> int:
        self.pointer += 1
        if self.pointer < len(self.arr):
            return self.arr[self.pointer]
    def hasNext(self) -> bool:
        if self.pointer + 1 < len(self.arr):
            return True
        return False
