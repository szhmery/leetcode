from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        ans = []
        n = len(num) - 1
        while n >= 0 or k > 0:
            value = k % 10 + num[n] + carry if n >= 0 else k % 10 + carry
            ans.append(value % 10)
            k //= 10
            carry = value // 10
            n -= 1
        if carry:
            ans.append(carry)
        return ans[::-1]

solution = Solution()

result = solution.addToArrayForm([1,2,3,4], 33)
print(result)