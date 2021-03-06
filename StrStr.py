class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        elif len(haystack) == 0 and len(needle) != 0:
            return -1
        else:
            return haystack.find(needle)

if __name__ == '__main__':
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    print(solution.strStr(haystack, needle))

    haystack = "aaaaa"
    needle = "bba"
    print(solution.strStr(haystack, needle))

    haystack = ""
    needle = ""
    print(solution.strStr(haystack, needle))

    haystack = ""
    needle = "ll"
    print(solution.strStr(haystack, needle))