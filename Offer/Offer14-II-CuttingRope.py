class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        MAX = 1000000007
        for i in range(3, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n] if dp[n] < MAX else dp[n] % MAX

    # https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/5vbrri/
    def cuttingRope2(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b, p = n // 3, n % 3, 1000000007
        if b == 0:
            return 3 ** a % p
        if b == 1:
            return 3 ** (a - 1) * 4 % p
        return 3 ** a * 2 % p

