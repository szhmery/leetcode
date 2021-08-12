class Solution:
    def __init__(self):
        self.valid = False

    def strToInt(self, str: str) -> int:
        if not str or len(str) == 0:
            return 0
        i = 0
        ans = 0
        sign = 1
        mx, mi, sign = 2 ** 31 - 1, -2 ** 31, 1
        while i < len(str):
            if str[i] == ' ':
                i += 1
            elif str[i] == '+':
                sign = 1
                i += 1
                break
            elif str[i] == '-':
                sign = -1
                i += 1
                break
            else:
                break
        while i < len(str):
            if str[i] >= '0' and str[i] <= '9':
                if ans > mx // 10 or (ans == mx // 10 and int(str[i]) > mx % 10):
                    ans = mx if sign > 0 else mi
                    return ans
                else:
                    ans = 10 * ans + int(str[i])
            else:
                break
            i += 1
        if i == len(str):
            self.valid = True
        return ans * sign

solution = Solution()
print(solution.strToInt('  -3'))
print(solution.strToInt('   -42'))
print(solution.strToInt('3444323423423423'))
print(solution.strToInt('-91283472332'))
print(solution.strToInt('-a3b'))
