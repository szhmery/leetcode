from collections import Counter


class Solution:
    #https://leetcode.com/problems/longest-palindrome/solution/
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        map = Counter(s)

        for v in map.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 != 0:  # aaaccc, if a is 3, add 1 more.
                ans += 1

        return ans


solution = Solution()
result = solution.longestPalindrome('abccb')
print(result)

result = solution.longestPalindrome('ccc')
print(result)

result = solution.longestPalindrome('cccaaadde')
print(result)
