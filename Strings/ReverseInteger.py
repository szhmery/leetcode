class Solution:
    def reverse(self, x: int) -> int:
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


if __name__ == '__main__':
    solution = Solution()
    x = 123
    result = solution.reverse(x)
    print("before reverse:{}".format(x))
    print("after reverse:{}".format(result))

    x = -123
    result = solution.reverse(x)
    print("before reverse:{}".format(x))
    print("after reverse:{}".format(result))

    x = 120
    result = solution.reverse(x)
    print("before reverse:{}".format(x))
    print("after reverse:{}".format(result))

    x = 0
    result = solution.reverse(x)
    print("before reverse:{}".format(x))
    print("after reverse:{}".format(result))

    x = 1534236469
    result = solution.reverse(x)
    print("before reverse:{}".format(x))
    print("after reverse:{}".format(result))
