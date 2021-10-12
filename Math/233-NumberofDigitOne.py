class Solution:
    # O(logN)
    # O(1)
    # https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/57nyhd/
    def countDigitOne(self, n: int) -> int:
        high = n
        low = 0
        cur = 0 # 当前位
        digit = 1
        count = 0
        while high != 0 or cur !=0:
            cur = high % 10
            high //= 10
            if cur == 0:
                count += high * digit # cur为0时, 1个数总是 high * digit
            elif cur == 1:
                count += high * digit + 1 + low
            else:
                count += (high + 1) * digit
            low = cur * digit + low
            digit *= 10
        return count

solution = Solution()
print(solution.countDigitOne(233))