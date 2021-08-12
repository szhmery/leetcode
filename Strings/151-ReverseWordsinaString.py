class Solution:
    # https://leetcode.com/problems/reverse-words-in-a-string/discuss/47973/Accepted-Python-answer-without-split()-join()-or-strip()
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        word = ''
        words = ''
        for i, c in enumerate(s):
            if c != ' ' and word != '' and s[i - 1] == ' ':
                words += word + ' '
                word = c
            elif c != ' ':
                word = c + word
            else:
                continue
        words += word
        return words

    def reverseWords2(self, s: str) -> str:
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        def clearSpace(s):
            i = 0
            j = 0
            n = len(s)
            while j < n:
                while j < n and s[j] == ' ':
                    j += 1
                while j < n and s[j] != ' ':
                    s[i] = s[j]
                    i += 1
                    j += 1
                while j < n and s[j] == ' ':
                    j += 1
                if j < n:
                    s[i] = ' '
                    i += 1

            return ''.join(s[:i])

        s = list(s)
        reverse(0, len(s) - 1)
        l = 0
        n = len(s)
        h = 0
        while h <= n and l < n:
            if s[l] == ' ':
                l += 1
                h += 1
            elif h == n or s[h] == ' ':
                reverse(l, h - 1)
                l = h
            else:
                h += 1
        print(s)
        return clearSpace(s)

    def reverseWords3(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


solution = Solution()
print(solution.reverseWords("  hello  world  "))
print(solution.reverseWords("I am a world!"))
