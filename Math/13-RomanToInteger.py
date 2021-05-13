class Solution:
    def romanToInt(self, s: str) -> int:
        # Symbol       Value
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 0
        for i in range(len(s) - 1):
            if roman_map[s[i]] < roman_map[s[i+1]]:
                count += 0 - roman_map[s[i]]
            else:
                count += roman_map[s[i]]
        count += roman_map[s[len(s) - 1]]
        return count


if __name__ == '__main__':
    solution = Solution()
    str_roman = 'IV'
    result = solution.romanToInt(str_roman)
    print('roman {0}, Int:{1}'.format(str_roman, result))
    str_roman = "LVIII"
    result = solution.romanToInt(str_roman)
    print('roman {0}, Int:{1}'.format(str_roman, result))