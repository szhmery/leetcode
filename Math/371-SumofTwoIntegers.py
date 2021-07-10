class Solution:
    #bit manipulation
    # https://blog.csdn.net/coder_orz/article/details/52034541
    def getSum(self, a: int, b: int) -> int:
        while b:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000 + 1)

    def getSum2(self, a: int, b: int) -> int:
        return a if b == 0 else self.getSum2(a ^ b, (a & b) << 1)


if __name__ == "__main__":
    solution = Solution()
    a = 13
    b = 3
    result = solution.getSum2(a, b)
    print(result)
    result = solution.getSum(2147483647, 2147483647)
    print(result)
    result = solution.getSum(2147483647, 2)
    print(result)

