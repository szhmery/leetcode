from collections import Counter


class Solution:
    # https://www.bilibili.com/video/BV1b541147WU
    def firstUniqChar2(self, s: str) -> int:
        ct = Counter(s)
        for i, c in enumerate(s):
            if ct[c] == 1:
                return i
        return -1

    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0

        for i in range(len(s)):
            if s.count(s[i]) > 1:
                continue
            else:
                return i
        return -1



if __name__ == '__main__':
    solution = Solution()
    s = "leetcode"
    index = solution.firstUniqChar(s)
    print("First unique character index: {}".format(index))
    index = solution.firstUniqChar2(s)
    print("Method 2: First unique character index: {}".format(index))
    s = "loveleetcode"
    index = solution.firstUniqChar(s)
    print("First unique character index: {}".format(index))

    s = "cc"
    index = solution.firstUniqChar(s)
    print("First unique character index: {}".format(index))

    s = "z"
    index = solution.firstUniqChar(s)
    print("First unique character index: {}".format(index))

    s = "aadadaad"
    index = solution.firstUniqChar(s)
    print("First unique character index: {}".format(index))
