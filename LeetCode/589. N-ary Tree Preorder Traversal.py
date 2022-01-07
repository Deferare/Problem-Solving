# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def preTravel(root):
            if root == None:
                return
            result.append(root.val)
            for i in range(len(root.children)):
                preTravel(root.children[i])
        result = []
        preTravel(root)
        return result
