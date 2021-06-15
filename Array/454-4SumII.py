from typing import List
from collections import defaultdict

class Solution:
    # https://www.bilibili.com/video/BV1ny4y1D7UL
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ct = defaultdict(int)
        for a in nums1:
            for b in nums2:
                ct[a + b] += 1
        res = 0
        for c in nums3:
            for d in nums4:
                if -(c+d) in ct:
                    res += ct[-(c+d)]
        return res


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    result = solution.fourSumCount(nums1, nums2, nums3, nums4)

    print(result)