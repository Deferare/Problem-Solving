class Node:
    def __init__(self, val = 0):
        self.val = val
        self.neighbors = []

from collections import deque
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        visited = {}
        copy_node = Node(node.val)
        visited[node.val] = copy_node
        q = deque([node])
        while len(q) > 0:
            current = q.popleft()
            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    copy_node = Node(neighbor.val)
                    visited[neighbor.val] = copy_node
                    q.append(neighbor)
                visited[current.val].neighbors.append(visited[neighbor.val])
        return visited[node.val]
