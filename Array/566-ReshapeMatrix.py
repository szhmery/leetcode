from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if r * c != row * col:
            return mat
        ans = [[0] * c for _ in range(r)]
        for i in range(r * c):
            ans[i // c][i % c] = mat[i // col][i % col]
        return ans

    def matrixReshape2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if r * c != row * col:
            return mat
        nums = []

        ans = [[0] * c for _ in range(r)]
        for i in range(row):
            for j in range(col):
                nums.append(mat[i][j])

        for i in range(r):
            for j in range(c):
                ans[i][j] = nums[c * i + j]
        return ans


solution = Solution()
mat = [[1, 2], [3, 4]]
r = 1
c = 4
result = solution.matrixReshape(mat, r, c)
print(result)
mat = [[1, 2], [3, 4]]
r = 2
c = 2
result = solution.matrixReshape(mat, r, c)
print(result)
mat = [[1, 2], [3, 4]]
r = 4
c = 1
result = solution.matrixReshape(mat, r, c)
print(result)

