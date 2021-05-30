class Solution:
    # two pointers
    # https://leetcode.com/problems/reverse-vowels-of-a-string/discuss/1239737/Python3-simple-solution-using-two-pointer-approach
    def reverseVowels(self, s: str) -> str:
        l = 0
        h = len(s) - 1
        s_list = list(s)
        vowel = {'a', 'e', 'i', 'o', 'u'}
        while l < h:
            while l < h and s_list[l].lower() not in vowel:
                l += 1
            while l < h and s_list[h].lower() not in vowel:
                h -= 1
            if s_list[l].lower() in vowel and s_list[h].lower() in vowel:
                s_list[l], s_list[h] = s_list[h], s_list[l]
                l += 1
                h -= 1
        return ''.join(s_list)


if __name__ == "__main__":
    solution = Solution()

    s = 'hello'
    print(solution.reverseVowels(s))
    s = ' '
    print(solution.reverseVowels(s))
