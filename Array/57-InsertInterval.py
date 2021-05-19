from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)
        if n == 0:
            return [newInterval]
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        ans.append([newInterval[0], newInterval[1]])
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]

    result = solution.insert(intervals, newInterval)
    print(result)

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    result = solution.insert(intervals, newInterval)
    print(result)