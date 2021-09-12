from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(r, c, oldColor, newColor):
            nonlocal image
            if r < 0 or r >= R or c < 0 or c >= C or image[r][c] != oldColor:
                return
            image[r][c] = newColor
            dfs(r + 1, c, oldColor, newColor)
            dfs(r, c + 1, oldColor, newColor)
            dfs(r - 1, c, oldColor, newColor)
            dfs(r, c - 1, oldColor, newColor)
            return

        if image[sr][sc] == newColor:
            return
        R = len(image)
        C = len(image[0])
        dfs(sr, sc, image[sr][sc], newColor)
        return image

    #BFD
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        R = len(image)
        C = len(image[0])
        image[sr][sc] = newColor
        queue = deque([(sr, sc)])
        while queue:
            (r, c) = queue.popleft()
            for i, j in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= i < R and 0 <= j < C and image[i][j] == oldColor:
                    queue.append((i, j))
                    image[i][j] = newColor
        return image


so = Solution()
print(so.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
print(so.floodFill2(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
print(so.floodFill2(image=[[0,0,0],[0,1,0]], sr=1, sc=1, newColor=1))

