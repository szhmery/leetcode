from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1VK411s7xi?from=search&seid=12872469680818489479
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res