class Solution:
    # https://www.bilibili.com/video/BV1ay4y1y7d2?from=search&seid=3393516485300897668
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        return len(s.split()[-1]) if s else 0

    def lengthOfLastWord2(self, s: str) -> int:
        length = 0
        pre_length = 0
        for i, c in enumerate(s):
            if c == ' ':
                if length != 0:
                    pre_length = length
                length = 0
                continue
            length += 1
        return length if c[-1] != " " else pre_length


if __name__ == '__main__':
    solution = Solution()
    s = "Hello World"
    result = solution.lengthOfLastWord(s)
    print(result)

    result = solution.lengthOfLastWord(" ")
    print(result)
    result = solution.lengthOfLastWord("a ")
    print(result)
    s = "b   a    "
    result = solution.lengthOfLastWord(s)
    print(result)