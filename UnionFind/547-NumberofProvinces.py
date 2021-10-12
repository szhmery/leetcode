from typing import List
import collections

class Solution:
    # 并查集
    # 时间复杂度：O(n^2 log n)，其中 nn 是城市的数量。需要遍历矩阵 isConnected 中的所有元素，时间复杂度是 O(n^2)，如果遇到相连关系，
    # 则需要进行 22 次查找和最多 11 次合并，一共需要进行 2n^2次查找和最多 n^2次合并，因此总时间复杂度是 O(2n^2 \log n^2)=O(n^2 \log n)。
    # 这里的并查集使用了路径压缩，但是没有使用按秩合并，最坏情况下的时间复杂度是 O(n^2 log n)，平均情况下的时间复杂度依然是 O(n^2 α(n))，
    # 其中 α 为阿克曼函数的反函数，α(n) 可以认为是一个很小的常数。
    # 空间复杂度：O(n)，其中 nn 是城市的数量。需要使用数组 parent 记录每个城市所属的连通分量的祖先。
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
        circles = set(find(i) for i in range(n))
        return len(circles)

    # DFS
    # 时间复杂度：O(n^2)，其中 n 是城市的数量。需要遍历矩阵n 中的每个元素。
    # 空间复杂度：O(n)，其中 n 是城市的数量。需要使用数组 visited 记录每个城市是否被访问过，数组长度是 n，递归调用栈的深度不会超过 n。
    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        def dfs(x):
            for j in range(n):
                if isConnected[x][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        n = len(isConnected)
        visited = set()
        circles = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                circles += 1
        return circles

    # BFS
    def findCircleNum3(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        circle = 0
        for k in range(n):
            if k not in visited:
                Q = collections.deque([k])
                while Q:
                    x = Q.popleft()
                    visited.add(x)
                    for i in range(n):
                        if isConnected[x][i] and i not in visited:
                            Q.append(i)
                circle += 1
        return circle


if __name__ == '__main__':
    solution = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result = solution.findCircleNum(isConnected)
    print(result)
    result = solution.findCircleNum2(isConnected)
    print(result)
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result = solution.findCircleNum3(isConnected)
    print(result)