from typing import List
import collections

class Solution:
    # DFS
    #时间复杂度：O(R×C)。其中 RR 是给定网格中的行数，CC 是列数。我们访问每个网格最多一次。
    #空间复杂度：O(R×C)，递归的深度最大可能是整个网格的大小，因此最大可能使用 O(R×C) 的栈空间。

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)


        R = len(grid)
        C = len(grid[0])
        seen = set()
        mx = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    mx = max(mx, dfs(i, j))
        return mx
    # DFS + stack
    # 把接下来想要遍历的土地放在栈里，然后在取出这些土地的时候访问它们。
    # 访问每一片土地时，我们将对围绕它四个方向进行探索，找到还未访问的土地，加入到栈 stack 中；
    # 另外，只要栈 stack 不为空，就说明我们还有土地待访问，那么就从栈中取出一个元素并访问
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        stack = []
        mx = 0
        for i, l in enumerate(grid):
            for j, val in enumerate(l):
                cur = 0
                stack.append((i, j))
                while stack:
                    r, c = stack.pop()
                    if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                        continue
                    cur += 1
                    grid[r][c] = 0
                    for di, dj in [[0, 1], [0, -1],[1, 0],[-1,0]]:
                        next_r, next_c = r + di, c + di
                        stack.append((next_r,next_c))
                mx = max(mx, cur)
    # BFS
    def maxAreaOfIsland3(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                cur = 0
                q = collections.deque([(i, j)])
                while q:
                    cur_i, cur_j = q.popleft()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        q.append((next_i, next_j))
                ans = max(ans, cur)
        return ans



so = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]


print(so.maxAreaOfIsland(grid))