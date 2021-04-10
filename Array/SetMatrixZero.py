from typing import List


class Solution:
    # Complexity Analysis
    # Time Complexity: O(M×N) where M and N are the number of rows and columns respectively.
    # Space Complexity: O(M + N).
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        row, col = set(), set()
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(R):
            for j in range(C):
                if i in row or j in col:
                    matrix[i][j] = 0


if __name__ == "__main__":
    solution = Solution()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution.setZeroes(matrix)
    print(matrix)
