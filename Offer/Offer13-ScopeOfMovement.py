class Solution:
    # dfs.
    # 19->20, 10-8=2
    # 20->21, 2 + 1 = 3
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
        visited = set()
        return dfs(0, 0, 0, 0)

    def movingCount2(self, m: int, n: int, k: int) -> int:

        queue = [(0,0,0,0)]
        visited = set()

        while queue:
            i, j, si, sj = queue.pop()
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))

        return len(visited)

    def movingCount3(self, m: int, n: int, k: int) -> int:
        def isInScope(row, col, k):
            sum_digits = 0
            while row:
                sum_digits += row % 10
                row //= 10
            while col:
                sum_digits += col % 10
                col //= 10
            if sum_digits > k:
                return False
            return True

        def dfs(row, col):
            nonlocal ans
            if row < 0 or row >= m or col < 0 or col >= n or (row, col) in visited or not isInScope(row, col, k):
                return 0
            visited.add((row,col))
            # ans += 1
            res = 1 + dfs(row + 1, col) + dfs(row, col + 1)
            # visited[row][col] = False
            return res
        visited = set()
        ans = 0
        res = dfs(0, 0)
        return res

so = Solution()
print(so.movingCount(2, 3, 1))
print(so.movingCount2(2, 3, 1))
print(so.movingCount3(2, 3, 1))
print(so.movingCount(16, 8, 4))
print(so.movingCount2(16, 8, 4))
print(so.movingCount3(16, 8, 4))