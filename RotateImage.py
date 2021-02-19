from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix)

        for i in range(width//2+width%2):
            for j in range(width//2):
                tmp = matrix[width-1-j][i]
                matrix[width-1-j][i] = matrix[width-1-i][width-1-j]
                matrix[width-1-i][width-1-j] = matrix[j][width-1-i]
                matrix[j][width-1-i] = matrix[i][j]
                matrix[i][j] = tmp






if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    print("after rotation:{}".format(matrix))
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix)
    print("after rotation:{}".format(matrix))