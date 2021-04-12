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

    # Complexity Analysis
    # Time Complexity: O(M×N) where M and N are the number of rows and columns respectively.
    # Space Complexity: O(1).
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0


if __name__ == "__main__":
    solution = Solution()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution.setZeroes(matrix)
    print(matrix)
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution.setZeroes2(matrix2)
    print(matrix2)
    matrix2 = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 1]]
    solution.setZeroes(matrix2)
    print(matrix2)
