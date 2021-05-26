from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = [0] * 26
        for i in range(len(s)):
            table[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            table[ord(t[i]) - ord('a')] -= 1
            if table[ord(t[i]) - ord('a')] < 0:
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        if t == s:
            return True
        else:
            return False

    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))
    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t))
