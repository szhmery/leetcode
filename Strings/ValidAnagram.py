class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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


if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))
    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t))
