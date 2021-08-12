from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, idx, word):
            if idx == len(word):
                return True
            if row < 0 or row >= R or col < 0 or col >= C or board[row][col] != word[idx]:
                return False
            # the second format
            # if row < 0 or row >= R or col < 0 or col >= C or board[row][col] != word[idx]:
            #     return False
            # if idx == len(word) - 1:
            #     return True
            c = board[row][col]
            board[row][col] = '#'
            res = dfs(row + 1, col, idx + 1, word) or \
                  dfs(row - 1, col, idx + 1, word) or \
                  dfs(row, col + 1, idx + 1, word) or \
                  dfs(row, col - 1, idx + 1, word)
            board[row][col] = c
            return res

        if not board or len(board[0]) == 0:
            return False
        R = len(board)
        C = len(board[0])
        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0, word):
                    return True
        return False
