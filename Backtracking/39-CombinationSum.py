from typing import List


class Solution:
    # back tracking
    # https://www.bilibili.com/video/BV1Jt411H75d?from=search&seid=10560058359354059971
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        element = []
        candidates.sort()
        self.DFS(ans, element, candidates, target, 0)
        return ans

    def DFS(self, ans, element, candidates, target, level):
        if target == 0:
            ans.append(element[::])
            return
        for i in range(level, len(candidates)):
            if target - candidates[i] >= 0:
                element.append(candidates[i])
                self.DFS(ans, element, candidates, target - candidates[i], i)
                element.pop()


if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    result = solution.combinationSum(candidates, target)
    print(result)
