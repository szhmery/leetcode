class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        i = 0
        j = 0
        while j < len(s):
            if j == len(s) - 1:
                ans += s[i:][::-1]
                break
            elif s[j] == ' ':
                ans += s[i:j][::-1] + ' '
                i = j + 1
                j += 1
            else:
                j += 1
        return ans

    def reverseWords2(self, s: str) -> str:
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        i, j = 0, 0
        s = list(s)
        while j <= len(s):
            if j == len(s) or s[j] == ' ' :
                reverse(i, j - 1)
                i = j + 1
                j += 1
            else:
                j += 1
        return ''.join(s)


    def reverseWords3(self, s: str) -> str:
        return ' '.join(x[::-1] for x in s.split())


solution = Solution()
print(solution.reverseWords(s="Let's take LeetCode contest"))
print(solution.reverseWords2(s="Let's take LeetCode contest"))
print(solution.reverseWords3(s="Let's take LeetCode contest"))
print(solution.reverseWords(s="God Ding"))
print(solution.reverseWords2(s="God Ding"))
print(solution.reverseWords3(s="God Ding"))
