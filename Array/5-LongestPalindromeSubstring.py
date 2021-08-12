class Solution:
    # https://www.bilibili.com/video/BV1so4y1o765?from=search&seid=1317791721071940273
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        st = i = max_len = 0
        while i < n:
            if n - i <= max_len // 2:
                break
            j = k = i
            while k < n - 1 and s[k+1] == s[k]:
                k += 1
            i = k + 1
            while k < n - 1 and j > 0 and s[k+1] == s[j-1]:
                k += 1
                j -= 1
            tmp = k - j + 1
            if max_len < tmp:
                st = j
                max_len = tmp
        return s[st:st+max_len]

    def longestPalindrome2(self, s: str) -> str:
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

    # DP
    #时间复杂度：O(n^2)，其中 nn 是字符串的长度。动态规划的状态总数为 O(n^2)，对于每个状态，我们需要转移的时间为 O(1)。
    #空间复杂度：O(n^2)，即存储动态规划状态需要的空间。

    def longestPalindrome_dp(self, s: str) -> str:
        n = len(s)
        if s is None or len(s) == 0:
            return None
        if n == 1:
            return s
        dp = [[False] * n for _ in range(n)]
        st = 0

        # for i in range(n):
        #     for j in range(n):
        #         if i == j:
        #             dp[i][j] = True
        #             st = i
        max_len = 1
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if max_len < j-i+1:
                        st = i
                        max_len = j-i+1
        return s[st:st+max_len]


if __name__ == '__main__':
    solution = Solution()
    s = "babad"
    result = solution.longestPalindrome(s)
    print(result)
    result = solution.longestPalindrome_dp(s)
    print(result)
