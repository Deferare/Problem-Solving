# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def postTravel(root):
            if root == None:
                return
            for i in range(len(root.children)):
                postTravel(root.children[i])
            result.append(root.val)
        result = []
        postTravel(root)
        return result
