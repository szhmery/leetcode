from typing import List
from collections import defaultdict

class Solution:
    # https://www.bilibili.com/video/BV1P441127pe?from=search&seid=5688692469542905848
    # https://www.bilibili.com/video/BV1jz411B7UJ?from=search&seid=5688692469542905848
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inbound = [0] * numCourses
        edge = defaultdict(list)
        for x, y in prerequisites:
            inbound[x] += 1
            edge[y].append(x)
        q = [i for i in range(numCourses) if inbound[i] == 0]
        visited = 0
        while q:
            cur = q.pop()
            visited += 1
            for n in edge[cur]:
                inbound[n] -= 1
                if inbound[n] == 0:
                    q.append(n)
        return visited == numCourses


if __name__ == "__main__":
    solution = Solution()
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    result = solution.canFinish(numCourses, prerequisites)
    print(result)
