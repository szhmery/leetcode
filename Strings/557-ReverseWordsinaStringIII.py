class Solution:
    #间复杂度：O(N)，其中 NN 为字符串的长度。原字符串中的每个字符都会在 O(1) 的时间内放入新字符串中。
    #空间复杂度：O(N)。我们开辟了与原字符串等大的空间。
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

    #时间复杂度：O(N)。字符串中的每个字符要么在 O(1) 的时间内被交换到相应的位置，要么因为是空格而保持不动。
    #空间复杂度：O(1)。因为不需要开辟额外的数组。
    def reverseWords2(self, s: str) -> str:
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        i, j = 0, 0
        s = list(s)
        while j <= len(s): # j equal the length, we can use the same parameter for reverse.
            if j == len(s) or s[j] == ' ': # put j == length in the first place
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
