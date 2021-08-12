class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        MAX = 1000000007
        for i in range(3, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n] if dp[n] < MAX else dp[n] % MAX