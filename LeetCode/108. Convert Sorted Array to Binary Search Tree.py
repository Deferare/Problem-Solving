# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def myRecursion(start, end):
            if start > end:
                return None
            mid = start+(end-start)//2
            root = TreeNode(nums[mid])
            root.left = myRecursion(start, mid-1)
            root.right = myRecursion(mid+1, end)
            return root

        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = myRecursion(0, mid-1)
        root.right = myRecursion(mid+1, len(nums)-1)
        return root
