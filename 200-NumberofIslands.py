from typing import List
from queue import Queue


class Solution:
    # DFS
    # https://www.bilibili.com/video/BV15A411n7Lg?from=search&seid=3015830509154272795
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.DFS(grid, i, j)
                    count += 1
        return count

    def DFS(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
            return
        grid[row][col] = '*'
        self.DFS(grid, row, col + 1)
        self.DFS(grid, row + 1, col)
        self.DFS(grid, row, col - 1)
        self.DFS(grid, row - 1, col)

    # BFS
    # https://www.bilibili.com/video/BV1SE411y7us?from=search&seid=3015830509154272795
    def numIslands2(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        queue = Queue()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '*'
                    queue.put([i, j])
                    self.BFS(grid, queue)
        return count

    def BFS(self, grid, queue):
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue.empty() is False:
            pos = queue.get()
            for direction in directions:
                row = pos[0] + direction[0]
                col = pos[1] + direction[1]
                if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
                    continue
                grid[row][col] = '*'
                queue.put([row, col])



if __name__ == '__main__':
    solution = Solution()
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    result = solution.numIslands(grid)
    print(result)
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    result = solution.numIslands2(grid)
    print(result)
