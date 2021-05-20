from typing import List


class Solution:
    def generate(self, n: int) -> List[List[int]]:
        # 方法1
        res = []
        for i in range(n):
            row = [1] * (i + 1)  # 小技巧，开始直接设置为全1
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res

    #https://leetcode.com/problems/pascals-triangle/solution/
    # DP
    def generate2(self, n: int) -> List[List[int]]:
        res = []
        for i in range(n):
            row = [None] * (i + 1)
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res


    def generate3(self, n: int) -> List[List[int]]:
        zong = [[1]]
        for i in range(1, n):  # 略过n==1时

            tt = zong[i - 1]
            # https://blog.csdn.net/puspos/article/details/102575182
            zong.append(list(map(lambda x, y: x + y, [0] + tt, tt + [0])))

        return zong[:n]  # [:n] == if n==0: return []

    # def generate(self, numRows: int) -> List[List[int]]:
    #     ans = []
    #     self.helper(numRows, ans)
    #     return ans
    #
    # def helper(self, numRows, ans: List):
    #     if numRows == 1:
    #         return ans.append([1])
    #     if numRows == 2:
    #         self.helper(numRows - 1, ans)
    #         ans.append([1, 1])
    #         return ans
    #     else:
    #         arr = ans[:-1]
    #         new_arr = [1]
    #         for i in range(len(arr)-1):
    #             new_arr.append(arr[i] + arr[i+1])
    #         new_arr.append([1])
    #         self.helper(numRows - 1, ans)
    #         ans.append(new_arr)


if __name__ == '__main__':
    solution = Solution()
    numRows = 5

    result = solution.generate(numRows)
    print(result)
    result = solution.generate2(numRows)
    print(result)
    result = solution.generate3(numRows)
    print(result)

