from typing import List
import bisect


class Solution:
    # https://www.bilibili.com/video/BV1aK4y1h7Bb
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        if R == 0:
            return False
        C = len(matrix[0])
        if C == 0:
            return False
        if matrix[0][0] > target or matrix[R - 1][C - 1] < target:
            return False
        tmp = []
        for i in range(R):
            tmp.append(matrix[i][0])
        ind = bisect.bisect_left(tmp, target)
        if ind == R:
            ind = ind - 1
        if target < matrix[ind][0]:
            ind = ind - 1
        ind2 = bisect.bisect_left(matrix[ind], target)
        if ind2 == C:
            return False
        return matrix[ind][ind2] == target


    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        if R == 0:
            return False

        C = len(matrix[0])
        if C == 0:
            return False
        if matrix[0][0] > target or matrix[R - 1][C - 1] < target:
            return False

        tmp = []
        for i in range(R):
            tmp.append(matrix[i][0])

        left = 0
        right = R - 1
        while left <= right:
            row = (left + right) // 2

            if tmp[row] == target:
                return True
            elif tmp[row] > target:
                right = row - 1
            else:
                left = row + 1
        if row == len(tmp):
            row = row - 1
        if target < matrix[row][0]:
            row = row - 1
        left = 0
        right = C - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        if R == 0:
            return False

        C = len(matrix[0])
        if C == 0:
            return False
        if matrix[0][0] > target or matrix[R - 1][C - 1] < target:
            return False

        l = 0
        r = R * C - 1
        while l <= r:
            mid = l + (r - l) // 2
            element = matrix[mid // C][mid % C]
            if element == target:
                return True
            elif element < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    result = solution.searchMatrix(matrix, target)
    print(result)
    result = solution.searchMatrix2(matrix, target)
    print(result)
    matrix = [[1, 3]]
    target = 1
    result = solution.searchMatrix3(matrix, target)
    print(result)
    result = solution.searchMatrix2(matrix, target)
    print(result)
