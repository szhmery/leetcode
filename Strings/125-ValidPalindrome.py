class Solution:
    # https://www.bilibili.com/video/BV17h411Z7ey
    # two pointers
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1

        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if lo < hi:
                if s[lo].lower() != s[hi].lower():
                    return False
                lo += 1
                hi -= 1

        return True

    def isPalindrome2(self, s: str) -> bool:
        tmp_str = ''
        s = s.lower()
        for i in range(len(s)):
            if s[i] >= 'a' and s[i] <= 'z' or s[i] >= '0' and s[i] <= '9':
                tmp_str = tmp_str + s[i]
            else:
                continue
        for j in range(len(tmp_str) // 2):
            if tmp_str[j] != tmp_str[len(tmp_str) - 1 - j]:
                return False
        return True
if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(s))
    s = "race a car"
    print(solution.isPalindrome2(s))
