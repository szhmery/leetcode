class Solution:
    # bit manipulation
    # https://www.bilibili.com/video/BV1qv411i7Wg?from=search&seid=4304170392741184236
    def reverseBits(self, n: int) -> int:
        ans = 0
        power = 31
        while n:
            ans += (n & 1) << power
            n >>= 1
            power -= 1

        return ans

    def reverseBits2(self, n: int) -> int:
        return int(bin(n)[2::].zfill(32)[::-1], 2)


if __name__ == '__main__':
    solution = Solution()
    n = 0b0010
    result = solution.reverseBits(n)
    print(result)
    solution = Solution()
    n = 0b0010
    result = solution.reverseBits2(n)
    print(result)