from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1hp4y1B7D5
    # 坐标映射
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in range(n):
            for j in range(m):
                live = 0
                for tx, ty in d:
                    x, y = i + tx, j + ty
                    if x < 0 or x == n or y < 0 or y == m:
                        continue
                    if board[x][y] & 1:
                        live += 1
                if board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 2
                else:
                    if 2 <= live <= 3:
                        board[i][j] = 3
                    else:
                        board[i][j] = 1
        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1
