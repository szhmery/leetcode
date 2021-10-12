class Solution:
    # https://www.bilibili.com/video/BV1TK4y1N72c?from=search&seid=5575991584373605738
    # two pointers
    # time complexity O(m*n)
    # space complexity O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack and needle:
            return -1
        h = n = 0
        while h < len(haystack):
            if haystack[h] == needle[n]:
                h += 1
                n += 1
                if n == len(needle):
                    return h - n
            else:
                h = h - n + 1
                n = 0
        return -1

    #sliding window
    def strStr2(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if m == 0: return 0

        for i in range(n - m + 1):
            j = 0
            idx = i
            while (i < n) and (j < m) and (haystack[i] == needle[j]):
                i += 1
                j += 1
            if j == m:
                return idx
        return -1

    def strStr_(self, haystack: str, needle: str) -> int:
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


    def strStr__(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

    # KMP
    # https://www.bilibili.com/video/BV18k4y1m7Ar/?spm_id_from=333.788.recommend_more_video.0
    def strStr3(self, s: str, p: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0: return 0

        lps = self.createlps(needle)
        # print("lps", lps)
        sp, pp = 0, 0
        while sp < n:
            # print(sp, pp)
            if haystack[sp] == needle[pp]:
                sp += 1
                pp += 1
            else:
                if pp == 0:
                    sp += 1
                else:
                    pp = lps[pp - 1]
            if pp == m:
                # print("pattern found starting at ", sp - pp)
                pp = lps[pp - 1]
                return sp - m
        return -1

    def createlps(self, p):
        lps = [0] * len(p)
        prefix = 0
        curr = 1
        while curr < len(p):
            if p[curr] == p[prefix]:
                lps[curr] = prefix + 1
                curr += 1
                prefix += 1
            else:
                if prefix == 0:
                    lps[curr] = 0
                    curr += 1
                else:
                    prefix = lps[prefix - 1]
        return lps


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