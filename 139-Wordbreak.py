from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1ba4y1n7c3?from=search&seid=14515994441351477989
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True  # 空串是可分
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]

    # https://www.bilibili.com/video/BV1p54y1k7vf
    # dp[i]表示s[:i]是否可分的，dp[len(s)]为所求
    # dp[i] = any(s[i - l]:i) == word and dp[i-l], l = len(word)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                l = len(w)
                if s[i - l : i] == w and dp[i - l]:
                    dp[i] = True
                    break
        return dp[-1]




if __name__ == '__main__':
    solution = Solution()
    s = "apple"
    wordDict = ["app", "le"]
    result = solution.wordBreak(s, wordDict)
    print(result)
    result = solution.wordBreak2(s, wordDict)
    print(result)

    s = "apele"
    wordDict = ["app", "le"]

    result = solution.wordBreak(s, wordDict)
    print(result)
    result = solution.wordBreak2(s, wordDict)
    print(result)
