class Solution:
    # https://leetcode.com/problems/convert-a-number-to-hexadecimal/discuss/89250/Python-solution
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        hexa = {}
        for i in range(10):
            hexa[i] = str(i)
        for i in range(10, 16):
            hexa[i] = chr(ord('a') + i - 10)
        ans = ''
        if num < 0:
            num = num + 2 ** 32  # add the max number
        while num:
            digit = num % 16
            ans = hexa[digit] + ans
            num = (num - digit) // 16

        return ans
    #https://leetcode.com/problems/convert-a-number-to-hexadecimal/discuss/89261/easy-10-line-python-solution-with-inline-explanation
    def toHex2(self, num: int) -> str:
        if num == 0:
            return '0'
        map_s = '0123456789abcdef'
        ans = ''
        for i in range(8):
            n = num & 15 #this means num & 1111b
            c = map_s[n]
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')


solution = Solution()
result = solution.toHex2(26)
print(result)

result = solution.toHex2(-1)
print(result)

result = solution.toHex2(-2)
print(result)
