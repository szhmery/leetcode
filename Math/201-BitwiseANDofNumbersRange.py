class Solution:
    #https://www.bilibili.com/video/BV1dT4y1g75m?from=search&seid=8111992973257838272
    # bit manipulation
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if len(bin(left)) != len(bin(right)):
            return 0
        bits = 0
        while left != right: # 找到相同bit的位數，其他不同的&之後都是0.
            left >>= 1
            right >>= 1
            bits += 1
        return left << bits


    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        ans = 2 ** 31 - 1
        for num in range(left, right + 1):
            ans = ans & num
        return ans

solution = Solution()
print(solution.rangeBitwiseAnd(5, 7))
print(solution.rangeBitwiseAnd(0, 0))
print(solution.rangeBitwiseAnd(0, 2147483647))