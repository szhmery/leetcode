class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        m, n = abs(dividend), abs(divisor)
        INT_MAX = pow(2, 31)
        result = 0
        while m >= n:
            t, p = n, 1
            while m >= (t << 1):
                t <<= 1
                p <<= 1
            result += p
            m -= t
        if (dividend < 0) ^ (divisor < 0):
            result = -result
        if result > INT_MAX - 1:
            return INT_MAX - 1
        elif result < -INT_MAX:
            return -INT_MAX
        else:
            return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.divide(27, 3)
    print(result)
