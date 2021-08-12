class Solution:
    def translateNum(self, num: int) -> int:
        #由于 dp[i] 只与 dp[i - 1] 有关，因此可使用两个变量 a,b 分别记录 dp[i], dp[i - 1]

        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a

