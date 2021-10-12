class Solution:
    # DP
    # https://leetcode-cn.com/problems/delete-operation-for-two-strings/solution/liang-ge-zi-fu-chuan-de-shan-chu-cao-zuo-14uw/
    # time O(nm)
    # space O(nm)
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if not word1 or not word2:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        # 可以计算两个字符串的最长公共子序列的长度，然后分别计算两个字符串的长度和最长公共子序列的长度之差
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs = dp[m][n]
        return m - lcs + n - lcs

    # https://leetcode-cn.com/problems/delete-operation-for-two-strings/solution/liang-ge-zi-fu-chuan-de-shan-chu-cao-zuo-14uw/
    # time O(nm)
    # space O(nm)
    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if not word1 or not word2:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        # 可以计算两个字符串的最长公共子序列的长度，然后分别计算两个字符串的长度和最长公共子序列的长度之差
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]

so = Solution()
print(so.minDistance("sea", "eat"))
print(so.minDistance2("sea", "eat"))