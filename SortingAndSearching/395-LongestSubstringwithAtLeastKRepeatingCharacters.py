from collections import Counter


class Solution:
    #https://www.bilibili.com/video/BV1hD4y1X7rq
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0

        for i in range(1, len(set(s)) + 1):
            l = r = ct = dif_ct = 0
            times = [0] * 26
            while r < len(s):
                # move right pointer
                ind = ord(s[r]) - ord('a')
                times[ind] += 1
                if times[ind] == 1:
                    dif_ct += 1
                if times[ind] == k:
                    ct += 1
                r += 1
                # move left pointer
                while l < r and dif_ct > i:
                    ind = ord(s[l]) - ord('a')
                    if times[ind] == k:
                        ct -= 1
                    if times[ind] == 1:
                        dif_ct -= 1
                    times[ind] -= 1
                    l += 1

                if dif_ct == ct == i:
                    res = max(res, r - l)
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "ababbc"
    k = 2
    result = solution.longestSubstring(s, k)
    print(result)