class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ''
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        carry = 0
        while n1 >= 0 or n2 >= 0:
            v1 = ord(num1[n1]) - ord('0') if n1 >= 0 else 0
            v2 = ord(num2[n2]) - ord('0') if n2 >= 0 else 0
            value = v1 + v2 + carry
            ans = str(value % 10) + ans
            carry = value // 10
            n1 -= 1
            n2 -= 1
        if carry:
            ans = str(carry) + ans
        return ans


solution = Solution()

result = solution.addStrings('11', '123')
print(result)
