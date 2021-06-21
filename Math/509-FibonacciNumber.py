class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def fib2(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        cur = 1
        pre = 1
        for i in range(3, n + 1):
            pre, cur = cur, pre + cur
        return cur


if __name__ == "__main__":
    solution = Solution()
    result = solution.fib(2)
    print(result)
    result = solution.fib(3)
    print(result)
    result = solution.fib(10)
    print(result)
    result = solution.fib2(10)
    print(result)
