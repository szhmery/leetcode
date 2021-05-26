from typing import List
from collections import Counter


class Solution:
    # https://www.bilibili.com/video/BV1LZ4y1M7Bg
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)
        maxc = max(ct.values())
        maxp = len([v for v in ct.values() if v == maxc])
        return max(len(tasks), (maxc - 1) * ( n + 1) + maxp)
