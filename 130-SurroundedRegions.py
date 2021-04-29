from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # https://www.bilibili.com/video/av65879006
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return
        row = len(board)
        col = len(board[0])
        for i in range(row):
            if board[i][0] == 'O':
                self.dfs(i, 0, board)
            if board[i][col - 1] == 'O':
                self.dfs(i, col - 1, board)
        for j in range(col):
            if board[0][j] == 'O':
                self.dfs(0, j, board)
            if board[row - 1][j] == 'O':
                self.dfs(row - 1, j, board)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'
    # DFS
    def dfs(self, i, j, board):
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
            return
        if board[i][j] != 'O':
            return

        board[i][j] = 'A'
        self.dfs(i + 1, j, board)
        self.dfs(i - 1, j, board)
        self.dfs(i, j + 1, board)
        self.dfs(i, j - 1, board)


if __name__ == '__main__':
    solution = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solution.solve(board)
    print(board)
