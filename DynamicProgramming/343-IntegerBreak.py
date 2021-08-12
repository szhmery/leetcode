import math
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


    def integerBreak2(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

    def integerBreak3(self, n: int) -> int:
        if n < 4:
            return n - 1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
so = Solution()
print(so.integerBreak(10))
print(so.integerBreak2(10))
print(so.integerBreak3(10))