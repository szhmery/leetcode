import sys

sys.setrecursionlimit(100000)


class Solution:
    # iterate, DP
    # https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/oxp3er/
    def lastRemaining(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i  # dp[i]=(dp[i−1]+m)%i
        return last

    # recursion
    def lastRemaining2(self, n: int, m: int) -> int:
        def f(n, m):
            if n == 0:
                return 0
            x = f(n - 1, m)
            return (x + m) % n

        if n < 1 or m < 1:
            return -1
        return f(n, m)


solution = Solution()
print(solution.lastRemaining(5, 4))
print(solution.lastRemaining2(5, 4))
print(solution.lastRemaining(5, 3))
print(solution.lastRemaining2(5, 3))
print(solution.lastRemaining(10, 17))
print(solution.lastRemaining2(10, 17))