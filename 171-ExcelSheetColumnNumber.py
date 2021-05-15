class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            num = ord(char) - ord('A') + 1
            ans = ans * 26 + num
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.titleToNumber("FXSHRXW")
    print(result)
    result = solution.titleToNumber("ZY")
    print(result)