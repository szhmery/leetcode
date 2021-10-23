class Solution:
    # time limit exceed
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    # 时间复杂度是O(m * n)，空间复杂度是O(m * n)
    def uniquePaths2(self, m: int, n: int) -> int:
        paths = [[0] * n for _ in range(m)]
        for i in range(m):
            paths[i][0] = 1
        for j in range(n):
            paths[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
        return paths[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    max_profilt = solution.uniquePaths2(3, 2)
    print(max_profilt)
    max_profilt = solution.uniquePaths2(3, 2)
    print(max_profilt)
