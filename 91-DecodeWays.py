class Solution:
    # DP
    # https://www.cnblogs.com/grandyang/p/4313384.html
    def numDecodings(self, s: str) -> int:
        if s is None or len(s) == 0 or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            dp[i] = 0 if s[i - 1] == '0' else dp[i - 1]
            if i > 1 and (s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6')):
                dp[i] += dp[i - 2]
        return dp[len(s)]


if __name__ == "__main__":
    solution = Solution()

    s = "226"

    result = solution.numDecodings(s)
    print(result)
