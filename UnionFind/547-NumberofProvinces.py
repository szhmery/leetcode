from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def find(x):
            if x == parents[x]:
                return parents[x]
            else:
                parents[x] = find(parents[x])
                return parents[x]

        def union(x, y):
            parents[find(x)] = find(y)

        n = len(isConnected)
        parents = list(range(n))
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    union(i, j)
        circle = set(find(i) for i in range(n))
        return len(circle)


if __name__ == '__main__':
    solution = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result = solution.findCircleNum(isConnected)
    print(result)
