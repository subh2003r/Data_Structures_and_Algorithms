from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        dq = deque()

        starting_pixel = image[sr][sc]
        
        if starting_pixel == color:
            return image

        dq.append((sr,sc))

        image[sr][sc] = color

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while dq:
            row, col = dq.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == starting_pixel:
                    image[nr][nc] = color
                    dq.append((nr, nc))

        return image
                    