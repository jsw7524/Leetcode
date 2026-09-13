class Solution:
    def DFS(self, image, y, x, original_color, new_color):
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for direction in directions:
            new_y = y + direction[0]
            new_x = x + direction[1]
            if new_y >= 0 and new_y < self.height and new_x >= 0 and new_x < self.width and image[new_y][new_x] == original_color:
                image[new_y][new_x] = new_color
                self.DFS(image, new_y, new_x, original_color, new_color)


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.height=len(image)
        self.width=len(image[0])
        original_color = image[sr][sc]
        if original_color != color:
            
            image[sr][sc] = color
            self.DFS(image, sr, sc, original_color, color)
        return image