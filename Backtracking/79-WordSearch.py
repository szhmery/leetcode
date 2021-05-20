from typing import List


class Solution:
    # DFS
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
            return False
        m = len(board)
        n = len(board[0])
        # !!!!This command doesn't work!!!!
        # visited = [[Flase] * n] * m
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.search(board, word, 0, i, j, visited):
                    return True
        return False

    def search(self, board, word, idx, i, j, visited_board):
        if idx == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited_board[i][j] or board[i][j] != word[idx]:
            return False
        visited_board[i][j] = True
        res = self.search(board, word, idx + 1, i - 1, j, visited_board) or \
              self.search(board, word, idx + 1, i + 1, j, visited_board) or \
              self.search(board, word, idx + 1, i, j - 1, visited_board) or \
              self.search(board, word, idx + 1, i, j + 1, visited_board)
        visited_board[i][j] = False
        return res

    # DFS, don't use visited
    def exist2(self, board: List[List[str]], word: str) -> bool:
        def search2(board, word, idx, i, j):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[idx]:
                return False
            c = board[i][j]
            board[i][j] = '#'
            res = search2(board, word, idx + 1, i - 1, j) or \
                  search2(board, word, idx + 1, i + 1, j) or \
                  search2(board, word, idx + 1, i, j - 1) or \
                  search2(board, word, idx + 1, i, j + 1)
            board[i][j] = c
            return res

        if len(board) == 0 or len(board[0]) == 0:
            return False
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if search2(board, word, 0, i, j):
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCC"

    result = solution.exist(board, word)
    print(result)
    result = solution.exist2(board, word)
    print(result)