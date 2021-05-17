from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(1, n * n + 1):
            matrix[r][c] = i

            cr = r + dr[di]
            cc = c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and matrix[cr][cc] == 0:
                r = cr
                c = cc
            else:
                di = (di + 1) % 4
                r = r + dr[di]
                c = c + dc[di]
        return matrix


if __name__ == "__main__":
    solution = Solution()

    result = solution.generateMatrix(3)
    print(result)




