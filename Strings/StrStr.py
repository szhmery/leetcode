class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        elif len(haystack) == 0 and len(needle) != 0:
            return -1
        else:
            return haystack.find(needle)

    def strStr2(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        m = len(haystack)
        n = len(needle)
        if m < n:
            return -1
        for i in range(m-n+1):
            if haystack[i] == needle[0]:
                for j in range(n):
                    if haystack[i+j] != needle[j]:
                        break
                if j == n - 1:
                    return i
        return -1


    def strStr3(self, haystack: str, needle: str) -> int:
        i = j = 0
        while 1:
            while 1:
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if needle[j] != haystack[i + j]:
                    break
                j += 1
            i += 1
        return -1
    def strStr3(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    print('method 1:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr(haystack, needle)))
    print('method 2:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr2(haystack, needle)))
    print('method 3:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr3(haystack, needle)))

    haystack = "aaaaa"
    needle = "bba"
    print('method 1:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr(haystack, needle)))
    print('method 2:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr2(haystack, needle)))
    print('method 3:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr3(haystack, needle)))

    haystack = ""
    needle = ""
    print('method 1:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr(haystack, needle)))
    print('method 2:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr2(haystack, needle)))
    print('method 3:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr3(haystack, needle)))

    haystack = ""
    needle = "ll"
    print('method 1:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr(haystack, needle)))
    print('method 2:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr2(haystack, needle)))
    print('method 3:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr3(haystack, needle)))

    haystack = "a"
    needle = "a"
    print('method 1:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr(haystack, needle)))
    print('method 2:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr2(haystack, needle)))
    print('method 3:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr3(haystack, needle)))

    haystack = "abc"
    needle = "c"
    print('method 1:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr(haystack, needle)))
    print('method 2:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr2(haystack, needle)))
    print('method 3:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr3(haystack, needle)))

    haystack = "mississippi"
    needle = "issip"
    print('method 1:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr(haystack, needle)))
    print('method 2:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr2(haystack, needle)))
    print('method 3:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr3(haystack, needle)))
    haystack = "mississippi"
    needle = "issipi"
    print('method 1:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr(haystack, needle)))
    print('method 2:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr2(haystack, needle)))
    print('method 3:haystack {0}, needle:{1}, index:{2}'.format(haystack, needle, solution.strStr3(haystack, needle)))