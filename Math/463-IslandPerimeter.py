from typing import List


class Solution:
    #https://www.bilibili.com/video/BV16V41167bF
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    res += 4
                    if i and grid[i - 1][j]: # don't use additional space
                        res -= 2 # it can also use d_lines
                    if j and grid[i][j - 1]:
                        res -= 2
        return res
    # space complexity 0(n*n), not good.
    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        island = set()
        d_lines = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count += 1
                    island.add((i, j))  #统计重复的边，每一个重叠边被重复算两次
                    if (i - 1, j) in island:
                        d_lines += 1
                    if (i, j - 1) in island:
                        d_lines += 1
        return count * 4 - 2 * d_lines


solution = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(solution.islandPerimeter(grid))
grid = [[1]]
print(solution.islandPerimeter(grid))
