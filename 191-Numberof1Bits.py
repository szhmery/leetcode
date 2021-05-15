class Solution:
    # https://www.bilibili.com/video/BV1i5411J7SA?from=search&seid=6359485431255227196
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += n & 1
            n >>= 1
        return ans

    def hammingWeight2(self, n: int) -> int:
        return bin(n).count("1")


if __name__ == '__main__':
    solution = Solution()
    n = 0b0010
    result = solution.hammingWeight(n)
    print(result)
    n = 0b11111111111111111111111111111101
    result = solution.hammingWeight(n)
    print(result)
    result = solution.hammingWeight2(n)
    print(result)