import math


class Solution:
    # Brute Force
    # Complexity Analysis
    # Time complexity : O(2^n). Size of recursion tree will be 2^n
    # Space complexity : O(n). The depth of the recursion tree can go upto n.
    def climbStairs(self, n: int) -> int:
        return self.climb_stair(0, n)

    def climb_stair(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_stair(i + 1, n) + self.climb_stair(i + 2, n)

    # Recursion with Memoization
    # Complexity Analysis
    # Time complexity : O(n). Size of recursion tree can go up to n.
    # Space complexity : O(n). The depth of recursion tree can go up to n.
    def climbStairs2(self, n: int) -> int:
        memo = [0 for i in range(n)]
        return self.climb_stair2(0, n, memo)

    def climb_stair2(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = (self.climb_stair2(i + 1, n, memo) + self.climb_stair2(i + 2, n, memo))
        return memo[i]

    # dynamic programming
    # Complexity Analysis
    # Time complexity : O(n). Single loop up to n.
    # Space complexity : O(n). dp array of size n is used.
    def climbStairs3(self, n):
        if n == 1:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # Fabonacci Number
    # Complexity Analysis
    # Time complexity : O(n). Single loop up to nn is required to calculate n th fibonacci number.
    # Space complexity : O(1). Constant space is used.
    def climbStairs4(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return third

    # Binets Method
    # Complexity Analysis
    # Time complexity : O(logn). Traversing on log n bits.
    # Space complexity : O(1). Constant space is used.
    def climbStairs5(self, n):
        q = [[1, 1], [1, 0]]
        res = self.pow(q, n)
        return res[0][0]

    def pow(self, a, n):
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if (n & 1) == 1:
                ret = self.multiply(ret, a)
            n = n >> 1
            a = self.multiply(a, a)
        return ret

    def multiply(self, a, b):
        tmp = [0 for j in range(2)]
        c = [tmp for i in range(2)]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c

    # Fibonacci Formula
    # Complexity Analysis
    # Time complexity : O(log n). powpow method takes log n time.
    # Space complexity : O(1). Constant space is used.

    def climbStairs6(self, n):
        sqr5 = float(math.sqrt(5))
        fibn = float(math.pow((1 + sqr5) / 2, n + 1) - math.pow((1 - sqr5) / 2, n + 1))
        return int(fibn / sqr5)


if __name__ == '__main__':
    solution = Solution()
    steps = solution.climbStairs(5)
    print(steps)
    steps = solution.climbStairs2(5)
    print(steps)
    steps = solution.climbStairs3(5)
    print(steps)
    steps = solution.climbStairs4(5)
    print(steps)
    steps = solution.climbStairs5(5)
    print(steps)
    steps = solution.climbStairs6(5)
    print(steps)
