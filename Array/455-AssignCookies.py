from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 2 3 4
        # 1 2 3
        g.sort()
        s.sort()
        lg, ls = len(g), len(s)
        i, j = 0, 0
        count = 0
        while j < ls and i < lg:
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count


solution = Solution()
g = [1, 2, 3]
s = [1, 1]
print(solution.findContentChildren(g, s))

g = [1, 2]
s = [1, 2, 3]
print(solution.findContentChildren(g, s))
