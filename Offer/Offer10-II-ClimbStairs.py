class Solution:
    def numWays(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n+1):
            a, b = a + b, a

        return a % 1000000007

so = Solution()
print(so.numWays(0))
print(so.numWays(1))