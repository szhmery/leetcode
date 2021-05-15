from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1Sv411L7qe?from=search&seid=4304961977438285074
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = 1
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] else obstacleGrid[i - 1][0]
        for j in range(1, n):
            obstacleGrid[0][j] = 0 if obstacleGrid[0][j] else obstacleGrid[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] else obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    steps = solution.uniquePathsWithObstacles(grid)
    print(steps)
