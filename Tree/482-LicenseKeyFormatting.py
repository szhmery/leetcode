class Solution:
    # https://leetcode.com/problems/license-key-formatting/discuss/96512/Java-5-lines-clean-solution
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] != '-':
                if len(ans) % (k + 1) == k:
                    ans.append('-')
                ans.append(s[i])

        return str(''.join(ans[::-1])).upper()
    #https://leetcode.com/problems/license-key-formatting/discuss/131978/beats-100-python3-submission
    def licenseKeyFormatting2(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        return '-'.join(s[i:i + k] for i in range(0, len(s), k))[::-1]

    def licenseKeyFormatting3(self, s: str, k: int) -> str:
        i = len(s) - 1
        ans = ''
        tmp = ''
        while i >= 0:
            if s[i] != '-':
                tmp = s[i].upper() + tmp
                if len(tmp) == k:
                    tmp = '-' + tmp
                    ans = tmp + ans
                    i -= 1
                    tmp = ''
                    continue
            i -= 1
        if not tmp:
            ans = ans[1:]
        else:
            ans = tmp + ans

        return ans


solution = Solution()
s = "2-5g-3-J"
k = 2
print(solution.licenseKeyFormatting(s, k))
print(solution.licenseKeyFormatting2(s, k))
s = "5F3Z-2e-9-w"
k = 4
print(solution.licenseKeyFormatting(s, k))
print(solution.licenseKeyFormatting2(s, k))
s = "2"
k = 2
print(solution.licenseKeyFormatting(s, k))
print(solution.licenseKeyFormatting2(s, k))
