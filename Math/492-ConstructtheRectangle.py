import math
from typing import List


class Solution:
    # https://leetcode.com/problems/construct-the-rectangle/discuss/97210/3-line-Clean-and-easy-understand-solution
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        return [area // w, w]

    def constructRectangle2(self, area: int) -> List[int]:
        if area <= 0:
            return
        ans = [area, 1]
        W = 1
        L = area
        while W <= math.sqrt(area):
            if area % W == 0:
                L = area // W
                if ans and L - W < ans[0] - ans[1]:
                    ans[0] = L
                    ans[1] = W
            W += 1
        return ans


solution = Solution()
print(solution.constructRectangle(122122))
print(solution.constructRectangle(37))
print(solution.constructRectangle(4))
