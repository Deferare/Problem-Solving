class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        image = image
        origin_color = image[sr][sc]
        y_len = len(image)
        x_len = len(image[0])
        def painter(index_y, index_x):
            key = str(index_y)+"|"+str(index_x)
            if key in visitied:
                return
            visitied[key] = 1
            if index_y >= y_len or index_x >= x_len or index_y < 0 or index_x < 0:
                return
            if image[index_y][index_x] != origin_color:
                return
            image[index_y][index_x] = newColor

            painter(index_y-1, index_x)
            painter(index_y, index_x+1)
            painter(index_y + 1, index_x)
            painter(index_y, index_x-1)

        visitied = {}
        painter(sr,sc)
        return image
