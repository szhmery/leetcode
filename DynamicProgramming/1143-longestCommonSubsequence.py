class Solution:
    # DP
    # https://leetcode-cn.com/problems/longest-common-subsequence/solution/fu-xue-ming-zhu-er-wei-dong-tai-gui-hua-r5ez6/
    # time O(nm)
    # space O(nm)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if not text1 or not text2:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:  # 当 text1[i - 1] == text2[j - 1] 时，说明两个子字符串的最后一位相等，所以最长公共子序列又增加了 1，所以 dp[i][j] = dp[i - 1][j - 1] + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  #  当 text1[i - 1] != text2[j - 1] 时，说明两个子字符串的最后一位不相等，那么此时的状态 dp[i][j] 应该是 dp[i - 1][j] 和 dp[i][j - 1] 的最大值。
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


so = Solution()
print(so.longestCommonSubsequence(text1="abcde", text2="ace"))
