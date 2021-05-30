from collections import Counter
from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ct_s = Counter(s)
        ct_t = Counter(t)
        for key in ct_t:
            if ct_t[key] != ct_s[key]:
                return key

    # https://www.bilibili.com/video/BV1f5411L7r4
    def findTheDifference2(self, s: str, t: str) -> str:
        dic = defaultdict(int)
        for key in s:
            dic[key] += 1
        for key in t:
            dic[key] -= 1
        for key in dic:
            if dic[key] != 0:
                return key


if __name__ == "__main__":
    solution = Solution()

    s = "aa"
    t = "aab"
    print(solution.findTheDifference(s, t))
    print(solution.findTheDifference2(s, t))
