class Solution:
    # https://www.bilibili.com/video/BV1JJ411A75u?from=search&seid=14248235482509120678
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        lines = [[] for _ in range(numRows)]
        index = 0
        while index < n:
            for i in range(numRows):
                if index < n:
                    lines[i].append(s[index])
                    index += 1
            for j in range(numRows-2, 0, -1):
                if index < n:
                    lines[j].append(s[index])
                    index += 1
        ans = ''
        for i in range(1, numRows):
            lines[0] += (lines[i])
        return ''.join(lines[0][i] for i in range(len(lines[0])) )

    # https://leetcode.com/problems/zigzag-conversion/solution/
    def convert2(self, s: str, numRows: int) -> str:
        if s == '' or s is None or numRows <= 0:
            return ''
        if numRows == 1:
            return s
        size = 2 * numRows - 2
        ans = ''
        for i in range(numRows):
            j = 0
            while j + i < len(s):
                ans += s[j + i]
                if i != 0 and i != numRows - 1 and j + size - i < len(s):
                    ans += s[j + size - i]
                j += size
        return ans

    def convert3(self, s: str, numRows: int) -> str:
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
    numRows = 4
    result = solution.convert(s, numRows)
    print(result)
    result = solution.convert2(s, numRows)
    print(result)
    result = solution.convert3(s, numRows)
    print(result)