class Solution:
    def intToRoman(self, num: int) -> str:
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD",
                       500: "D", 900: "CM", 1000: "M"}
        ans = ''
        key_set = sorted(numeral_map.keys())
        while num > 0:
            for key in reversed(key_set):
                while num // key > 0:
                    num -= key
                    ans += numeral_map[key]
        return ans


if __name__ == '__main__':
    solution = Solution()
    num = 3999
    result = solution.intToRoman(num)
    print('Int {0}, Roman:{1}'.format(num, result))