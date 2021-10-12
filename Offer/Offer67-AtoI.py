class Solution:
    def strToInt(self, str: str):
        str = str.strip()  # 删除首尾空格
        if not str:  # 字符串为空直接返回
            return 0
        res, i, sign = 0, 1, 1
        int_max, int_min = 2 ** 31 - 1, -2 ** 31
        if str[0] == '-':  # 保存负号
            sign = -1
        elif str[0] != '+':  # 若无符号位， 则需从 i = 0 开始数字拼接
            i = 0
        for c in str[i:]:
            if not '0' <= c <= '9':  # 遇到非数字的字符则跳出
                break
            if res > int_max // 10 or res == int_max // 2 and c > '7':
                return int_max if sign == 1 else int_min
            res = res * 10 + ord(c) - ord('0')  # 数字拼接
        return sign * res

    def __init__(self):
        self.valid = False

    def strToInt2(self, str: str) -> int:
        if not str or len(str) == 0:
            return 0
        i = 0
        ans = 0
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
                    ans = 10 * ans + ord(str[i]) - ord('0')
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
