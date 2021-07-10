class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = list(a)
        b = list(b)
        ans = ''
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            ans = str((carry % 2)) + ans
            carry //= 2
        return ans

    # https://www.bilibili.com/video/BV1Q5411h7gc
    def addBinary2(self, a: str, b: str) -> str:
        def add(x, y, carry):
            s = x + y + carry
            return (s // 2, s % 2)

        maxlen = max(len(a), len(b))
        carry = 0
        a = a.rjust(maxlen, '0')
        b = b.rjust(maxlen, '0')
        ans = ''
        for i in range(maxlen - 1, -1, -1):
            carry, s = add(int(a[i]), int(b[i]), carry)
            ans = str(s) + ans
        return '1' + ans if carry else ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.addBinary2('1101', '100')
    print(result)
