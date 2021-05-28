class Solution:
    # DP
    # https://www.bilibili.com/video/BV12C4y1h7Ao?from=search&seid=17640066302150177237
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    result = solution.numTrees(3)
    print(result)
    result = solution.numTrees(5)
    print(result)
