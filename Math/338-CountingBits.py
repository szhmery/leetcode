from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1VK411s7xi?from=search&seid=12872469680818489479
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

    def numberof1(self,n: int):
        ans = 0
        while n:
            ans += 1
            n = (n - 1) & n
        return ans

if __name__ == '__main__':
    solution = Solution()
    result = solution.countBits(3)
    print(result)
    result = solution.numberof1(9)
    print(result)