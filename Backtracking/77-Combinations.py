from typing import List


class Solution:
    # backtracking
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(first, cur):
            if len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(first, n + 1):
                if i in cur:
                    continue
                cur.append(i)
                helper(i + 1, cur)
                cur.pop()

        ans = []
        helper(1, [])
        return ans


if __name__ == '__main__':
    solution = Solution()
    n = 4
    k = 2
    result = solution.combine(n, k)
    print(result)

