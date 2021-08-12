from enum import Enum


class Solution:
    def isNumber(self, s: str) -> bool:
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END"
        ])
        Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_SPACE",
            "CHAR_ILLEGAL"
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch == "+" or ch == "-":
                return Chartype.CHAR_SIGN
            elif ch == " ":
                return Chartype.CHAR_SPACE
            else:
                return Chartype.CHAR_ILLEGAL

        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_SPACE: State.STATE_INITIAL,
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN
            },
            State.STATE_INT_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
            },
            State.STATE_INTEGER: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_EXP: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN
            },
            State.STATE_EXP_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_END: {
                Chartype.CHAR_SPACE: State.STATE_END
            },
        }

        st = State.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]

        return st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER,
                      State.STATE_END]



class Solution2:
    # https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/
    def isNumber(self, s: str) -> bool:
        states = [
            {' ': 0, 's': 1, 'd': 2, '.': 4},  # 0. start with 'blank'
            {'d': 2, '.': 4},  # 1. 'sign' before 'e'
            {'d': 2, '.': 3, 'e': 5, ' ': 8},  # 2. 'digit' before 'dot'
            {'d': 3, 'e': 5, ' ': 8},  # 3. 'digit' after 'dot'
            {'d': 3},  # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            {'s': 6, 'd': 7},  # 5. 'e'
            {'d': 7},  # 6. 'sign' after 'e'
            {'d': 7, ' ': 8},  # 7. 'digit' after 'e'
            {' ': 8}  # 8. end with 'blank'
        ]
        p = 0  # start with state 0
        for c in s:
            if '0' <= c <= '9':
                t = 'd'  # digit
            elif c in "+-":
                t = 's'  # sign
            elif c in "eE":
                t = 'e'  # e or E
            elif c in ". ":
                t = c  # dot, blank
            else:
                t = '?'  # unknown
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)


    #https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/jian-zhi-offer-20-biao-shi-shu-zhi-de-zi-060v/
    def isNumber2(self, s: str) -> bool:
        n = len(s)
        index = 0
        has_num = has_e = has_sign = has_dot = False
        while index < n and s[index] == ' ':
            index += 1
        while index < n:
            while index < n and '0' <= s[index] <= '9':
                index += 1
                has_num = True
            if index == n:
                break
            if s[index] == 'e' or s[index] == 'E':
                if has_e or not has_num:
                    return False
                has_e = True
                has_num = has_sign = has_dot = False
            elif s[index] == '+' or s[index] == '-':
                if has_sign or has_num or has_dot:
                    return False
                has_sign = True
            elif s[index] == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif s[index] == ' ':
                break
            else:
                return False
            index += 1
        while index < n and s[index] == ' ':
            index += 1
        return has_num and index == n


    # def isNumber(self, s: str) -> bool:
        # def isDecimal(i):
        #     if s[i] == '+' or s[i] == '-':
        #         i += 1
        #     if i >= n:
        #         return [False, i]
        #     if s[i] == '.':
        #         i += 1
        #         if i >= n:
        #             return [False, i]
        #         if not(ord('0') <= ord(s[i]) <= ord('9')):
        #             return [False, i]
        #         while i < n:
        #             if ord('0') <= ord(s[i]) <= ord('9'):
        #                 i += 1
        #                 continue
        #             else:
        #                 return [True, i]
        #     elif ord('0') <= ord(s[i]) <= ord('9'):
        #         while i < n:
        #             if ord('0') <= ord(s[i]) <= ord('9'):
        #                 i += 1
        #                 continue
        #             elif s[i] == '.':
        #                 i += 1
        #                 if i >= n:
        #                     return [False, i]
        #                 if not (ord('0') <= ord(s[i]) <= ord('9')):
        #                     return [False, i]
        #                 while i < n:
        #                     if ord('0') <= ord(s[i]) <= ord('9'):
        #                         i += 1
        #                         continue
        #                     else:
        #                         return [True, i]
        #             else:
        #                 [False, i]
        #     else:
        #         return [False, i]
        #
        #
        # def isInteger(i):
        #     if s[i] == '+' or s[i] == '-':
        #         i += 1
        #     if i >= n:
        #         return [False, i]
        #     if not(ord('0') <= ord(s[i]) <= ord('9')):
        #         return [False, i]
        #     while i < n:
        #         if ord('0') <= ord(s[i]) <= ord('9'):
        #             i += 1
        #             continue
        #         else:
        #             return [True, i]
        #
        # if not s:
        #     return False
        # i = 0
        # n = len(s)
        # while i < n:
        #     if s[i] != ' ':
        #         break
        # if i >= n:
        #     return False
        # tmp = i
        # res1, i1 = isDecimal(tmp)
        # res2, i2 = isInteger(tmp)
        # if not (res1, res2):
        #     return False
        # if res1:
        #     i = i1
        # else:
        #     i = i2
        # if s[i] == 'e' or s[i] == 'E':
        #     i += 1
        #     tmp = i
        #     res3, i3 = isInteger(tmp)
        #     if not res3:
        #         return False
        #     i = i3
        # while i < n:
        #     if s[i] == ' ':
        #         i += 1
        #         continue
        #     else:
        #         break
        # return i == n



so = Solution()
print(so.isNumber(''))
print(so.isNumber('.'))
print(so.isNumber('0'))
print(so.isNumber('3'))
print(so.isNumber('e'))
print(so.isNumber('  .1  '))
print(so.isNumber('  .e  '))