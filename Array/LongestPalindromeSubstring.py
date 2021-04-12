class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) < 1:
            return ''
        start = end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1


if __name__ == '__main__':
    solution = Solution()
    s = "babad"
    result = solution.longestPalindrome(s)
    print(result)
