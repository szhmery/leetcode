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

    # reiterate
    # https://www.bilibili.com/video/BV1Lb411y7ec?from=search&seid=17718863427344375264
    def numDecodings2(self, s: str) -> int:
        def decode(s, l, r):
            if l in ways:
                return ways[l]
            if l < n and s[l] == '0':
                return 0
            if l >= r:
                return 1

            w = decode(s, l + 1, r)
            if 10 <= int(s[l: l + 2]) <= 26:
                w += decode(s, l + 2, r)
            ways[l] = w
            return w

        ways = {}
        n = len(s)
        if n == 0:
            return 0
        return decode(s, 0, n - 1)


if __name__ == "__main__":
    solution = Solution()

    s = "226"

    result = solution.numDecodings(s)
    print(result)
    result = solution.numDecodings2(s)
    print(result)
