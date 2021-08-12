class Solution:
    #https://leetcode.com/problems/reverse-string-ii/discuss/100890/Python-Straightforward-with-Explanation
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i+k] = s[i:i+k][::-1]
        return ''.join(s)
    #wrong solution
    # def reverseStr2(self, s: str, k: int) -> str:
    #     def reverse(start, end):
    #         while start < end:
    #             s[start], s[end] = s[end], s[start]
    #             start += 1
    #             end -= 1
    #
    #     if len(s) < k:
    #         return s
    #
    #     s = list(s)
    #     if len(s) == k:
    #         reverse(0, len(s) - 1)
    #         return ''.join(s)
    #
    #     i = 0
    #     j = k - 1
    #     while j < len(s):
    #         reverse(i, j)
    #         i += 2 * k
    #         j += 2 * k
    #     return ''.join(s)


solution = Solution()
print(solution.reverseStr(s="abcdefg", k=2))
print(solution.reverseStr(s="abcdefg", k=8))
print(solution.reverseStr(s="abcd", k=4))
