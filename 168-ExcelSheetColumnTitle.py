class Solution:
    # https://www.bilibili.com/video/BV1Qj411f7FY?from=search&seid=816482609626242780
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber -= 1 # not start with 0
            tmp = columnNumber % 26
            ans = ans + chr(tmp + ord('A'))
            columnNumber = (columnNumber // 26)
        return ans[::-1]

if __name__ == '__main__':
    solution = Solution()
    result = solution.convertToTitle(701)
    print(result)
    result = solution.convertToTitle(2147483647)
    print(result)
