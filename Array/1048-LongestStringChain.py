from typing import List


class Solution:
    # https://www.bilibili.com/video/BV17K4y1G7et
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word: len(word))
        dict = {}
        res = 0
        for word in words:
            cur = 1
            for i in range(len(word)):
                tmp = word[:i] + word[i + 1:]
                if tmp in dict:
                    cur = max(cur, dict[tmp] + 1)
            dict[word] = cur
            res = max(res, cur)
        return res


if __name__ == "__main__":
    solution = Solution()
    words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    result = solution.longestStrChain(words)

    print(result)
