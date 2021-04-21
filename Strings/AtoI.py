import math


class Solution:
    def myAtoi(self, s: str) -> int:
        tmp_str = ''
        is_negative = False

        # step 1:
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            else:
                tmp_str = s[i:]
                break
        # step 2:
        if len(tmp_str) == 0:
            return 0
        if tmp_str[0] == '-':
            is_negative = True
            tmp_str = tmp_str[1:]
        elif tmp_str[0] == '+':
            is_negative = False
            tmp_str = tmp_str[1:]
        # step 3:
        tmp2_str = ''
        for j in range(len(tmp_str)):
            if tmp_str[j] < str(0) or tmp_str[j] > str(9):
                break
            else:
                tmp2_str = tmp_str[:j + 1]
                continue
        # step 4:
        if len(tmp2_str) == 0:
            return 0
        else:
            if is_negative:
                return_num = int('-' + tmp2_str)
            else:
                return_num = int(tmp2_str)
        # step 5:
        if return_num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif return_num < -2 ** 31:
            return -2 ** 31
        else:
            return return_num

    def myAtoi2(self, s: str) -> int:
        i = 0
        sign = 1
        result = 0
        MAX_VALUE = 2 ** 31 - 1
        MIN_VALUE = -2 ** 31
        if len(s) == 0:
            return 0
        # Discard whitespaces in the beginning
        while i < len(s) and s[i] == ' ':
            i += 1
        # check if optional sign if it exits
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        # build the result and check for overflow/underflow condition
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            if result > MAX_VALUE // 10 or (result == MAX_VALUE // 10 and int(s[i]) > MAX_VALUE % 10):
                return MAX_VALUE if sign == 1 else MIN_VALUE
            result = result * 10 + int(s[i])
            i += 1

        return result * sign

if __name__ == '__main__':
    solution = Solution()
    s = "42"
    result = solution.myAtoi2(s)
    print("myatoi: {0} -> {1}".format(s, result))
    s = "   -42"
    result = solution.myAtoi2(s)
    print("myatoi: {0} -> {1}".format(s, result))
    s = "4193 with words"
    result = solution.myAtoi2(s)
    print("myatoi: {0} -> {1}".format(s, result))
    s = "words and 987"
    result = solution.myAtoi2(s)
    print("myatoi: {0} -> {1}".format(s, result))
    s = "-91283472332"
    result = solution.myAtoi2(s)
    print("myatoi: {0} -> {1}".format(s, result))
    s = " "
    result = solution.myAtoi2(s)
    print("myatoi: {0} -> {1}".format(s, result))
