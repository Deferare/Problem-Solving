# Definition for a Node.
class Node:
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

from collections import deque
saveNext = deque()
class Solution:
    def flatten(self, head: Node) -> Node:
        def myDFS(node):
            global saveNext
            if node == None:
                if len(saveNext) > 0:
                    return myDFS(saveNext.popleft())
                return None
            if node.child != None:
                saveNext.appendleft(node.next)
                crnt = myDFS(node.child)
                node.child = None
            else:
                crnt = myDFS(node.next)
            node.next = crnt
            if crnt != None:
                crnt.prev = node
            return node
        myDFS(head)
        return head
