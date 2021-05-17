class Solution:
    def lengthOfLastWord(self, s: str) -> int:
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