class Solution:
    # two points are wrong. Because s1, s2 may have same chars, we can't separate them
    # DP
    # https://leetcode-cn.com/problems/interleaving-string/solution/jiao-cuo-zi-fu-chuan-by-leetcode-solution/
    # time O(nm)
    # space O(nm)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        n = len(s1)
        m = len(s2)
        if len(s3) != n + m:
            return False

        f = [[None] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                p = i + j - 1
                if i > 0:
                    f[i][j] = f[i][j] or f[i - 1][j] and s1[i - 1] == s3[p]
                if j > 0:
                    f[i][j] = f[i][j] or f[i][j - 1] and s2[j - 1] == s3[p]
        return f[n][m]

    # 使用滚动数组优化空间复杂度。 因为这里数组 f 的第 i 行只和第 i−1 行相关，所以我们可以用滚动数组优化这个动态规划，
    # 这样空间复杂度可以变成 O(m)
    # time O(nm)
    # space O(m)
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if len(s3) != len(s1) + len(s2):
            return False
        n = len(s1)
        m = len(s2)
        f = [None] * (m + 1)
        f[0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                p = i + j - 1
                if i > 0:
                    f[j] = f[j] and s1[i - 1] == s3[p]
                if j > 0:
                    f[j] = f[j] or (f[j - 1] and s2[j - 1] == s3[p])
        return f[m]

    # https://leetcode-cn.com/problems/interleaving-string/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/
    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if (len1 + len2 != len3):
            return False
        dp = [[False] * (len2 + 1) for i in range(len1 + 1)]
        dp[0][0] = True
        for i in range(1, len1 + 1):  # 表示 s1 的前 i 位是否能构成 s3 的前 ii 位
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        for i in range(1, len2 + 1):  # 表示 s2 的前 i 位是否能构成 s3 的前 i 位
            dp[0][i] = (dp[0][i - 1] and s2[i - 1] == s3[i - 1])
        # s1 的前 i 个字符和 s2 的前 j−1 个字符能否构成 s3 的前 i+j−1 位，且 s2 的第 j 位（s2[j−1]）是否等于 s3 的第 i+j 位 s3[i+j−1]。
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                            dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return dp[-1][-1]



so = Solution()
print(so.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
print(so.isInterleave2(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))

