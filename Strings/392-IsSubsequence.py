import bisect
from collections import defaultdict


class Solution:
    # two pointers
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == len(s) else False
    #     https://www.bilibili.com/video/BV1Za4y1a73v
    def isSubsequence2(self, s: str, t: str) -> bool:
        q = list(s)
        for c in t:
            if not q:
                return True
            if c == q[0]:
                q.pop(0)
        return not q
    # follow up, use dict to store t and binary search to find the next position
    # https://www.bilibili.com/video/BV1Za4y1a73v
    def isSubsequence3(self, s: str, t: str) -> bool:
        dic = defaultdict(list)
        for i, c in enumerate(t):
            dic[c].append(i)
        cur = -1
        for c in s:
            if c not in dic:
                return False
            l = dic[c]
            p = bisect.bisect_left(l, cur)
            if p == len(l):
                return False
            cur = l[p] + 1
        return True


if __name__ == "__main__":
    solution = Solution()

    s = "abc"
    t = "ahbgdc"
    print(solution.isSubsequence(s, t))
    print(solution.isSubsequence2(s, t))
    print(solution.isSubsequence3(s, t))
    s = "axc"
    t = "ahbgdc"
    print(solution.isSubsequence(s, t))
    print(solution.isSubsequence2(s, t))
    print(solution.isSubsequence3(s, t))