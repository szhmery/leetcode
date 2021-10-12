class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000 + 1)

    # n=a⊕b 非进位和：异或运算
    # c=a&b<<1 进位：与运算+左移一位
    # s=a+b⇒s=n+c
    def getSum2(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


    # wrong answer
    def getSum3(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7ffffffff else ~(a ^ x)

        # x = 0xffffffff
        # a, b = a & x, b & x
        # while b != 0:
        #     a, b = (a ^ b), (a & b) << 1 & x
        # return a if a <= 0x7fffffff else ~(a ^ x)







solution = Solution()
print(solution.getSum(13, 3))
print(solution.getSum(-1, -1))
print(solution.getSum(2147483646, 1))
print(solution.getSum(2147483647, 1))

print(solution.getSum2(13, 3))
print(solution.getSum2(-1, -1))
print(solution.getSum2(2147483646, 1))
print(solution.getSum2(2147483647, 1))
