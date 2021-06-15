from typing import List
import heapq
from bisect import bisect

class Solution:
    # https://www.bilibili.com/video/BV1qt411L7ZS?from=search&seid=16475192415886611409
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j + 1], i ,j + 1))
        return ret

    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if sum(bisect(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    result = solution.kthSmallest(matrix, k)
    print(result)

    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    result = solution.kthSmallest2(matrix, k)
    print(result)
