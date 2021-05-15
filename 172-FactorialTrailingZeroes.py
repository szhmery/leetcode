class Solution:
    def trailingZeroes(self, n: int) -> int:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        ans = 0
        while factorial > 0:
            if factorial % 10 != 0:
                break
            else:
                ans += 1
                factorial //= 10

        return ans

    # https://www.bilibili.com/video/BV1hE411n7TM?from=search&seid=13562143442051016125
    def trailingZeroes2(self, n: int) -> int:
        ans = 0
        while n >= 5:
            n = n // 5
            ans += n
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.trailingZeroes(5)
    print(result)

    result = solution.trailingZeroes2(5)
    print(result)

    result = solution.trailingZeroes(3)
    print(result)

    result = solution.trailingZeroes(0)
    print(result)

    result = solution.trailingZeroes2(10)
    print(result)
