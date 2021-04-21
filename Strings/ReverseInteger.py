class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))

        ans = int(s[::-1]) if x > 0 else -int(s[::-1])
        if ans >= 2 ** 31 - 1 or ans <= -2 ** 31:
            return 0
        return ans

    def reverse2(self, x: int) -> int:
        x = str(x)
        y = ''
        if x[0] == '-':
            y = '-'
            for i in range(1, len(x)):
                y = y + x[len(x) - i]

        else:
            for i in range(len(x)):
                y = y + x[len(x) - 1 - i]

        y = int(y)
        if y >= 2 ** 31 - 1 or y <= -2 ** 31:
            return 0
        return y

    def reverse3(self, x: int) -> int:
        ans = 0
        MAX_VALUE = 2 ** 31 - 1
        MIN_VALUE = -2 ** 31
        while x != 0:
            pop = x % 10
            x //= 10

            if ans > MAX_VALUE // 10 or (ans == MAX_VALUE//10 and pop > 7):
                return 0
            if ans < MIN_VALUE // 10 or (ans == MIN_VALUE//10 and pop < -8):
                return 0
            ans = ans * 10 + pop
        return ans


if __name__ == '__main__':
    solution = Solution()
    n = 123
    result = solution.reverse3(n)
    print('n: {0}, result:{1}'.format(n, result))
