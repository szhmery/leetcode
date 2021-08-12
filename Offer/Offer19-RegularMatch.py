class Solution:
    #https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/zhu-xing-xiang-xi-jiang-jie-you-qian-ru-shen-by-je/
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1): # If p is null, the result is False. Calculate from 1.

                if p[j-1] != '*':
                    if i > 0 and (s[i-1] == p[j-1] or p[j-1] == '.'):
                        dp[i][j] |= dp[i-1][j-1]
                else:
                    if j >= 2:
                        dp[i][j] |= dp[i][j - 2]
                    if i >= 1 and j >= 2 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                        dp[i][j] |= dp[i-1][j]

        return dp[m][n]

so = Solution()
print(so.isMatch('aaa','ab*.*'))
print(so.isMatch('','.'))
