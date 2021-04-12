class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_list = []
        length = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            longest_substring = ''
            for j in range(i, len(s)):
                if s[j] not in longest_substring:
                    longest_substring += s[j]
                else:
                    break
            substring_list.append(longest_substring)

        for substring in substring_list:
            length = max(length, len(substring))
        return length

    def lengthOfLongestSubstring2(self, s: str) -> int:
        longest_substring = ''
        length = 0
        for c in s:
            if c in longest_substring:
                index = longest_substring.index(c)
                if index == len(longest_substring) - 1:
                    longest_substring = c
                else:
                    longest_substring = longest_substring[index+1:] + c
            else:
                longest_substring += c
            length = max(length, len(longest_substring))

        return length

    def lengthOfLongestSubstring3(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            # mp[s[j]] = j
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

    def lengthOfLongestSubstring4(self, s: str) -> int:
        chars = [None] * 128
        left = right = 0
        ans = 0
        while right < len(s):
            r = ord(s[right])
            index = chars[r]
            if index != None and index >= left and index < right:
                left = index + 1
            chars[r] = right

            ans = max(ans, right - left + 1)
            right += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring3(s)
    print(result)
    s = " "
    result = solution.lengthOfLongestSubstring4(s)
    print(result)
    s = "aab"
    result = solution.lengthOfLongestSubstring3(s)
    print(result)
    s = "aab"
    result = solution.lengthOfLongestSubstring2(s)
    print(result)
    s = "dvdf"
    result = solution.lengthOfLongestSubstring3(s)
    print(result)
    s = "abba"
    result = solution.lengthOfLongestSubstring3(s)
    print(result)