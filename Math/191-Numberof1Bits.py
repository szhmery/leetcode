class Solution:
    # bit manipulation
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count
    # https://www.bilibili.com/video/BV1i5411J7SA?from=search&seid=6359485431255227196
    def hammingWeight2(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += n & 1
            n >>= 1
        return ans

    def hammingWeight3(self, n: int) -> int:
        return bin(n).count("1")


if __name__ == '__main__':
    solution = Solution()

    print(solution.hammingWeight(0b0010))
    print(solution.hammingWeight2(0b0010))
    print(solution.hammingWeight(0b11111111111111111111111111111101))
    print(solution.hammingWeight2(0b11111111111111111111111111111101))
    print(solution.hammingWeight3(0b11111111111111111111111111111101))
