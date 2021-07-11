class Solution:
    #https://leetcode.com/problems/number-of-segments-in-a-string/solution/
    def countSegments(self, s: str) -> int:
        return len(s.split())

    def countSegments2(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                count += 1
        return count
    def countSegments3(self, s: str) -> int:
        if len(s) == 0:
            return 0
        count = 0
        pre = " "
        for c in s:
            if c == ' ' and pre != ' ':
                count += 1
            pre = c
        if s[-1] != ' ':
            count += 1
        return count

solution = Solution()
print(solution.countSegments("Hello, my name is John"))
print(solution.countSegments2("Hello, my name is John"))
print(solution.countSegments(""))
print(solution.countSegments(""))
print(solution.countSegments("                "))
print(solution.countSegments2("                "))