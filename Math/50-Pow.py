class Solution:
    # time limit exceeded
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n > 0:
            while n > 0:
                ans = ans * x
                n -= 1
        elif n == 0:
            return 1
        else:
            x = 1 / x
            n = abs(n)
            while n > 0:
                ans = ans * x
                n -= 1
        return ans

    # https://blog.csdn.net/fuxuemingzhu/article/details/82960833
    # recursive
    def myPow2(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow2(x, -n)
        if n % 2 == 1:
            return x * self.myPow2(x, n - 1)
        else:
            cur = self.myPow2(x, n / 2)
            return cur * cur

    # iterative
    def myPow3(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            if n % 2:
                ans *= x
            n >>= 1
            x *= x
        return ans


if __name__ == '__main__':
    solution = Solution()
    x = 2.00000
    n = 4
    result = solution.myPow(x, n)
    print(result)
    n = 5
    result = solution.myPow(x, n)
    print(result)
    n = 10
    result = solution.myPow(x, n)
    print(result)
    result = solution.myPow(2, 10)
    print(result)
    result = solution.myPow2(2.0, -2)
    print(result)
    result = solution.myPow3(2.0, 5)
    print(result)
    result = solution.myPow3(2.0, -2)
    print(result)
