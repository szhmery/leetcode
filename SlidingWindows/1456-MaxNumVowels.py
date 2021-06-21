from collections import defaultdict
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        vowels = {'a','e', 'i', 'o', 'u'}
        counts = 0
        for i in range(k):
            if s[i] in vowels:
                counts += 1
        ans = max(ans, counts)
        for i in range(k, n):
            if s[k] in vowels:
                counts += 1
            if s[i - k] in vowels:
                counts -= 1
            ans = max(ans, counts)
        return ans


if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    k = 3
    result = solution.maxVowels(s, k)
    print(result)
    s = "abciiidef"
    k = 3
    result = solution.maxVowels(s, k)
    print(result)
    s = "weallloveyou"
    k = 7
    result = solution.maxVowels(s, k)
    print(result)
    s = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
    k = 33
    result = solution.maxVowels(s, k)
    print(result)