from typing import List
from collections import defaultdict


class Solution:
    # https://www.bilibili.com/video/BV1qt4y1X7oC?from=search&seid=8680116968263755374
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        inbound = [0] * numCourses
        edge = defaultdict(list)
        for x, y in prerequisites:
            inbound[x] += 1
            edge[y].append(x)
        q = [i for i in range(numCourses) if inbound[i] == 0]

        ans = []
        while q:
            cur = q.pop()
            ans.append(cur)
            for n in edge[cur]:
                inbound[n] -= 1
                if inbound[n] == 0:
                    q.append(n)
        return ans if len(ans) == numCourses else []


if __name__ == "__main__":
    solution = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = solution.findOrder(numCourses, prerequisites)
    print(result)

