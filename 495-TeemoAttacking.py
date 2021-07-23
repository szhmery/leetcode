from typing import List


class Solution:
    # https://leetcode.com/problems/teemo-attacking/solution/
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(1, len(timeSeries)):
            tmp = timeSeries[i] - timeSeries[i - 1]
            ans += tmp if tmp <= duration else duration
            #ans += min(tmp, duration) # time cost is higher
        return ans + duration

solution = Solution()
print(solution.findPoisonedDuration([1, 4], 2))
print(solution.findPoisonedDuration([1, 2], 2))
