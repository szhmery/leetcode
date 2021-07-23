class Solution:
    #https://www.bilibili.com/video/BV1Lg4y167NB
    def findComplement(self, num: int) -> int:
        x = 1
        while x <= num:
            x <<= 1
        return (x - 1) ^ num

    def findComplement2(self, num: int) -> int:
        ans = 0
        i = 0
        while num > 0:
            ans |= ((num & 1) ^ 1) << i
            i += 1
            num >>= 1
        return ans

solution = Solution()
print(solution.findComplement(5))
print(solution.findComplement(1))
print(solution.findComplement(6))
