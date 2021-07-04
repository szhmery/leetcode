# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:

        # write your code in Python 3.6
        if n == 1:
            return [0]
        ans = []
        ans.extend([x for x in range(1, n // 2 + 1)])
        ans.extend([-x for x in range(1, n // 2 + 1)])
        if len(ans) != n:
            ans.append(0)
        return ans

    def sumZero2(self, n: int) -> List[int]:
        return list(range(1 - n, n, 2))


if __name__ == "__main__":
    solution = Solution()

    print(solution.sumZero(5))
    print(solution.sumZero(1))
    print(solution.sumZero(4))

    print(solution.sumZero2(5))
    print(solution.sumZero2(1))
    print(solution.sumZero2(4))