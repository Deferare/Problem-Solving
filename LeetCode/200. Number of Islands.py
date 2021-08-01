class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_len_x = len(grid[0])
        grid_len_y = len(grid)

        def land_checker(index_y, index_x):
            if index_x >= grid_len_x or index_y >= grid_len_y or index_x < 0 or index_y < 0:
                return
            key = str(index_y)+"|"+str(index_x)
            visited[key] = 1
            if grid[index_y][index_x] == "0":
                return
            right_key = str(index_y+1)+"|"+str(index_x)
            left_key = str(index_y)+"|"+str(index_x-1)
            top_key = str(index_y-1)+"|"+str(index_x)
            down_key = str(index_y)+"|"+str(index_x+1)

            if right_key not in visited:
                land_checker(index_y+1,index_x)
            if left_key not in visited:
                land_checker(index_y, index_x-1)
            if top_key not in visited:
                land_checker(index_y-1, index_x)
            if down_key not in visited:
                land_checker(index_y, index_x+1)

        result_cnt = 0
        visited = {}
        for i in range(grid_len_y):
            for j in range(grid_len_x):
                key = str(i) + "|" + str(j)
                if key not in visited and grid[i][j] == "1":
                    result_cnt += 1
                    land_checker(i,j)
        return result_cnt
