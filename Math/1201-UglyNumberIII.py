class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        if n <= 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        t1, t2, t3 = 0, 0, 0
        for i in range(1, n + 1):
            dp[i] = min(dp[t1] * a, dp[t2] * b, dp[t3] * c)
            while dp[t1] * a <= dp[i]:
                t1 += 1
            while dp[t2] * b <= dp[i]:
                t2 += 1
            while dp[t3] * c <= dp[i]:
                t3 += 1
        return dp[n]


solution = Solution()
print(solution.nthUglyNumber(n=3, a=2, b=3, c=5))
print(solution.nthUglyNumber(n=5, a=2, b=11, c=13))
