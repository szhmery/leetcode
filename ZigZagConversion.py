class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == '' or s is None or numRows <= 0:
            return ''
        if numRows == 1:
            return s
        size = 2 * numRows - 2
        ans = ''
        for i in range(numRows):
            for j in range(i, len(s), size):
                ans += s[j]
                if i != 0 and i != numRows - 1 and j - i + size - i < len(s):
                    ans += s[j - i + size - i]
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    result = solution.convert(s, numRows)
    print(result)
