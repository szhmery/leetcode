class Solution:
    # https://www.bilibili.com/video/BV1Yt4y1S7XZ?from=search&seid=5964199382172656577
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)

    # https://leetcode.com/problems/repeated-substring-pattern/discuss/94352/Java-Simple-Solution-with-Explanation
    def repeatedSubstringPattern2(self, s: str) -> bool:
        if not s or len(s) == 0:
            return False
        n = len(s)
        for length in range(n // 2, 0, -1):
            if n % length != 0:
                continue
            count = n // length
            pattern = s[0: length]
            i = 1
            while i < n:
                if s[i * length:i * length + length] != pattern:
                    break
                i += 1
            if i == count:
                return True
        return False

    # https://leetcode.com/problems/repeated-substring-pattern/discuss/94352/Java-Simple-Solution-with-Explanation
    def repeatedSubstringPattern3(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return False

        for length in range(1, n // 2 + 1):  # pattern must repeat at least twice, i.e. pattern length is at most n/2
            if n % length != 0:  # s length must can be divided by the pattern length
                continue
            pattern = s[0:length]  # pattern string
            i = length  # start index of 2nd pattern
            j = i + length - 1  # // end index of 2nd pattern
            while j < n:
                sub_s = s[i:j + 1]
                if pattern != sub_s:  # failed for this pattern, try next pattern
                    break
                i += length
                j += length
            if i == n:  # if it past the last substring check, i will be n
                return True
        return False


solution = Solution()
print(solution.repeatedSubstringPattern('abab'))
print(solution.repeatedSubstringPattern('aba'))
print(solution.repeatedSubstringPattern('abcabcabcabc'))
print(solution.repeatedSubstringPattern2('abab'))
print(solution.repeatedSubstringPattern2('aba'))
print(solution.repeatedSubstringPattern2('abac'))
print(solution.repeatedSubstringPattern2('abcabcabcabc'))
print(solution.repeatedSubstringPattern3('abab'))
print(solution.repeatedSubstringPattern3('aba'))
print(solution.repeatedSubstringPattern3('abcabcabcabc'))
