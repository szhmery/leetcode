from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1ba4y1n7c3?from=search&seid=14515994441351477989
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]


if __name__ == '__main__':
    solution = Solution()
    s = "apple"
    wordDict = ["app", "le"]

    result = solution.wordBreak(s, wordDict)
    print(result)
    s = "apele"
    wordDict = ["app", "le"]

    result = solution.wordBreak(s, wordDict)
    print(result)
