from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1S5411x7mi?from=search&seid=9802513906260437230
    # all possible means to use backtracking
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        if s is None or len(s) == 0:
            return ans
        ans = []
        curr = []
        self.helper(s, ans, curr, 0)
        return ans

    def helper(self, s, ans, curr, low):
        if low == len(s):
            ans.append(curr[::])
            return
        n = len(s)
        for i in range(low, n):
            if self.isPalinedrome(s, low, i):
                curr.append(s[low:i+1])
                self.helper(s, ans, curr, i + 1)
                curr.pop()

    def isPalinedrome(self, s, lo, hi):
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "aab"

    result = solution.partition(s)
    print(result)
