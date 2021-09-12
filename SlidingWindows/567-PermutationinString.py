class Solution:
    #时间复杂度：O(n+m+|\Sigma|)O(n+m+∣Σ∣)，其中 nn 是字符串 s1的长度，mm 是字符串 s2 的长度，\SigmaΣ 是字符集，这道题中的字符集是小写字母，
    # |\Sigma|=26∣Σ∣=26。
    # 空间复杂度：O(|\Sigma|)O(∣Σ∣)。
    # slice windows
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        chars1 = [0] * 26
        chars2 = [0] * 26
        n1, n2 = len(s1), len(s2)
        for i in range(n1): # two arrays to store n1 length of data
            chars1[ord(s1[i]) - ord('a')] += 1
            chars2[ord(s2[i]) - ord('a')] += 1

        if chars2 == chars1: # compare them
            return True
        i = 0
        for j in range(n1, n2): # slice windows move forward one by one. From n1 to n2
            chars2[ord(s2[j - n1]) - ord('a')] -= 1 # remove the left one. The length is n1
            chars2[ord(s2[j]) - ord('a')] += 1 # add the right one.
            i += 1
            if chars1 == chars2:
                return True
        return False

so = Solution()
print(so.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
print(so.checkInclusion(s1 = "ab", s2 = "eidboaooo"))
print(so.checkInclusion(s1 = "adc", s2 = "dcda"))