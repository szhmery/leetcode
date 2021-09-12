from typing import List
from collections import deque

class Solution:
    # 时间复杂度：O(rc)，其中 r 为矩阵行数，c 为矩阵列数，即矩阵元素个数。广度优先搜索中每个位置最多只会被加入队列一次，因此只需要 O(rc) 的时间复杂度。
    # 空间复杂度：O(rc)，其中 r 为矩阵行数，c 为矩阵列数，即矩阵元素个数。除答案数组外，最坏情况下矩阵里所有元素都为 00，全部被加入队列中，此时需要 O(rc) 的空间复杂度。
    # BFS
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        R = len(mat)
        C = len(mat[0])
        seen = set()
        queue = deque()
        dict = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0: # 找到所有0，再往外层一层一层增加1
                    queue.append((r, c))
                    seen.add((r, c))
        while queue:
            i, j = queue.popleft()
            for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen:
                    dict[ni][nj] = dict[i][j] + 1
                    queue.append((ni, nj))
                    seen.add((ni, nj))
        return dict

so = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(so.updateMatrix(mat))
