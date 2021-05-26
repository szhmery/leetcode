class Solution:
    # https://blog.csdn.net/coder_orz/article/details/52034541
    def getSum(self, a: int, b: int) -> int:
        while b:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)


if __name__ == "__main__":
    solution = Solution()
    a = 1
    b = 2
    result = solution.getSum(a, b)
    print(result)

