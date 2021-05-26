from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1ay4y1J7or?from=search&seid=4115778426468700531
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])
        row = 0
        col = n_col - 1
        while row < n_row and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    result = solution.searchMatrix(matrix, target)
    print(result)
