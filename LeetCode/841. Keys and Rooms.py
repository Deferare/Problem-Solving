class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}
        def recursion(room):
            visited[room] = 1
            for crnt in rooms[room]:
                if crnt not in visited:
                    recursion(crnt)
        recursion(0)
        if len(visited) != len(rooms):
            return False
        return True
