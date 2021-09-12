from typing import List


class Solution:
    # 自顶向下
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * (n)  # 我们从 i 到 0 递减地枚举 j，这样我们只需要一个长度为 n 的一维数组 dp，就可以完成状态转移。
        dp[0] = triangle[0][0]

        for i in range(1, n):
            dp[i] = dp[i - 1] + triangle[i][i]  # 第i排最后一个
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]  # 第i排第一个
        return min(dp)

    # 我们将任一点到底边的最小路径和，转化成了与该点相邻两点到底边的最小路径和中的较小值，再加上该点本身的值
    # 将解法二中「自顶向下的递归」改为「自底向上的递推」
    # 空间优化为O(N)
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]

    # 时间复杂度：O(N^2), N 为三角形的行数。
    # 空间复杂度：O(N^2),N 为三角形的行数。
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]


so = Solution()
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(so.minimumTotal2(triangle))
triangle = [[-1], [2, 3], [1, -1, -3]]
print(so.minimumTotal2(triangle))
