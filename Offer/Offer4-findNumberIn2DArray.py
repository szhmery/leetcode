from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        R = len(matrix)
        C = len(matrix[0])
        if R == 0 or C == 0 or target < matrix[0][0] or target > matrix[R-1][C-1]:
            return False
        row = 0
        col = len(matrix[0]) - 1
        ans = False
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                ans = True
                break
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return ans

    # binary search, it can't use here, because the num in previous row may be bigger than the current row.
    def findNumberIn2DArray2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        R = len(matrix)
        C = len(matrix[0])
        if target < matrix[0][0] or target > matrix[R-1][C-1]:
            return False
        tmp = []
        for i in range(R):
            tmp.append(matrix[i][0])
        i = 0
        j = R - 1
        while i <= j:
            row = i + (j - i) // 2
            if tmp[row] == target:
                return True
            elif tmp[row] < target:
                i = row + 1
            else:
                j = row - 1
        if row == R:
            row = R - 1
        if target < matrix[row][0]:
            row -= 1
        i = 0
        j = C - 1
        while i <= j:
            mid = i + (j - i)// 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False

solution = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(solution.findNumberIn2DArray(matrix, 5))
print(solution.findNumberIn2DArray2(matrix, 5))
