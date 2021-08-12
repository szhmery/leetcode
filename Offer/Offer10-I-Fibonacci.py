import sys
from collections import defaultdict

sys.setrecursionlimit(100000)


class Solution:
    def __init__(self):
        self.list = defaultdict()

    def fib(self, n: int) -> int:
        MAX = int(1e9 + 7)
        a, b = 0, 1
        for i in range(n):
            a, b = a + b, a
            if a >= MAX:
                a %= MAX
        return a

    def fib2(self, n: int) -> int:
        MAX = 1e9 + 7
        if n <= 1:
            self.list[n] = n
            return n
        if n in self.list:
            return self.list[n]
        res = self.fib(n - 1) + self.fib(n - 2)
        if res >= MAX:
            res %= MAX
        self.list[n] = res
        return res


so = Solution()
print(so.fib2(2))
print(so.fib2(45))
