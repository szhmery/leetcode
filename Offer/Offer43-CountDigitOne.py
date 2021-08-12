class Solution:
    #时间复杂度 O(logn) ： 循环内的计算操作使用 O(1) 时间；循环次数为数字 n 的位数，即 Nlog 10n ，因此循环使用 O(logn) 时间。
    #空间复杂度 O(1) ： 几个变量使用常数大小的额外空间。
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:#当 cur = 0 时： 此位 1 的出现次数只由高位 high 决定，计算公式为：high×digit
                res += high * digit
            elif cur == 1:#当 cur = 1 时： 此位 1 的出现次数由高位 high 和低位 low 决定，计算公式为：high×digit+low+1
                res += high * digit + low + 1
            else:#当 cur=2,3,⋯,9 时： 此位 1 的出现次数只由高位 high 决定，计算公式为：(high+1)×digit
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res

