from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1JC4y1x7j1?from=search&seid=5366533450486511202
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(0, m):
            for j in range(0, n):
                dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    steps = solution.minPathSum(grid)
    print(steps)
