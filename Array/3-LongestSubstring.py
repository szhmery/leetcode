class Solution:
    # slicing window
    # use array, save count
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        char_map = [0] * 256
        lo = 0
        length = 0
        for hi in range(len(s)):
            char_map[ord(s[hi])] += 1
            while char_map[ord(s[hi])] > 1: # check the hi position, if hi is the duplicate value, move lo one by one
                char_map[ord(s[lo])] -= 1  # move lo, reduce the count of lo, not hi.
                lo += 1
            length = max(length, hi - lo + 1)
        return length

    # use set, save char
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        char_set = set()
        lo = 0
        length = 0
        for hi in range(len(s)):
            if s[hi] in char_set:
                while lo < hi and s[lo] != s[hi]: # 不断地移动右指针，不要删除两者相等的那个，要保留，不然就没有了。
                    char_set.remove(s[lo])
                    lo += 1
                lo += 1
            else:
                char_set.add(s[hi])
            length = max(length, hi - lo + 1)
        return length

    # use dict, save index
    def lengthOfLongestSubstring3(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                # i = max(mp[s[j]], i) # if save index + 1
                i = max(mp[s[j]] + 1, i) # find the existing index and plus 1.
            mp[s[j]] = j
            ans = max(ans, j - i + 1)
            # mp[s[j]] = j + 1 # if save index + 1

        return ans

    # use array, save index
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

    """
      # wrong!
       def lengthOfLongestSubstring_wrong(self, s: str) -> int:
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
           """


if __name__ == '__main__':
    solution = Solution()
    s = "abba"
    print("source string 1:{}".format(s))
    result = solution.lengthOfLongestSubstring(s)
    print("method 1:{}".format(result))
    result = solution.lengthOfLongestSubstring2(s)
    print("method 2:{} ".format(result))
    result = solution.lengthOfLongestSubstring3(s)
    print("method 3:{}".format(result))
    result = solution.lengthOfLongestSubstring4(s)
    print("method 4:{}".format(result))

    s = " "
    print("source string 2:{}".format(s))
    result = solution.lengthOfLongestSubstring(s)
    print("method 1:{}".format(result))
    result = solution.lengthOfLongestSubstring2(s)
    print("method 2:{}".format(result))
    result = solution.lengthOfLongestSubstring3(s)
    print("method 3:{}".format(result))
    result = solution.lengthOfLongestSubstring4(s)
    print("method 4:{}".format(result))

    s = "aab"
    print("source string 3:{}".format(s))
    result = solution.lengthOfLongestSubstring(s)
    print("method 1:{}".format(result))
    result = solution.lengthOfLongestSubstring2(s)
    print("method 2:{}".format(result))
    result = solution.lengthOfLongestSubstring3(s)
    print("method 3:{}".format(result))
    result = solution.lengthOfLongestSubstring4(s)
    print("method 4:{}".format(result))

    s = "dvdf"
    print("source string 4:{}".format(s))
    result = solution.lengthOfLongestSubstring(s)
    print("method 1:{}".format(result))
    result = solution.lengthOfLongestSubstring2(s)
    print("method 2:{}".format(result))
    result = solution.lengthOfLongestSubstring3(s)
    print("method 3:{}".format(result))
    result = solution.lengthOfLongestSubstring4(s)
    print("method 4:{}".format(result))

    s = "pwwkew"
    print("source string 5:{}".format(s))
    result = solution.lengthOfLongestSubstring(s)
    print("method 1:{}".format(result))
    result = solution.lengthOfLongestSubstring2(s)
    print("method 2:{}".format(result))
    result = solution.lengthOfLongestSubstring3(s)
    print("method 3:{}".format(result))
    result = solution.lengthOfLongestSubstring4(s)
    print("method 4:{}".format(result))

    s = "tmmzuxt"
    print("source string 6:{}".format(s))
    result = solution.lengthOfLongestSubstring(s)
    print("method 1:{}".format(result))
    result = solution.lengthOfLongestSubstring2(s)
    print("method 2:{}".format(result))
    result = solution.lengthOfLongestSubstring3(s)
    print("method 3:{}".format(result))
    result = solution.lengthOfLongestSubstring4(s)
    print("method 4:{}".format(result))