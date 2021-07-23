class Solution:
    #https://www.bilibili.com/video/BV1M5411Y79g
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
    
    def hammingDistance2(self, x: int, y: int) -> int:
        tmp = x ^ y
        count = 0
        while tmp > 0:
            count += tmp & 1
            tmp >>= 1
        # while tmp:
        #     tmp = tmp & (tmp - 1)
        #     count += 1
        return count

solution = Solution()
print(solution.hammingDistance(2, 4))
print(solution.hammingDistance(1, 3))