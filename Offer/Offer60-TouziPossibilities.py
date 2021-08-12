from typing import List
import  math

class Solution:

    def dicesProbability(self, n: int) -> List[float]:
        kMaxPoint = 6
        dp = [1 / kMaxPoint] * kMaxPoint

        for i in range(2, n + 1):
            tmp = [0] * ((kMaxPoint - 1) * i + 1)
            for j in range(len(dp)):
                for k in range(kMaxPoint):
                    tmp[j + k] += dp[j]/ kMaxPoint
            dp = tmp
        return dp
    # force brute
    def dicesProbability2(self, n: int) -> List[float]:

        def Probalities(original, cur, points):
            if cur == 1:
                counts[points - original] += 1
            else:
                for j in range(1, kMaxPoint + 1):
                    Probalities(original, cur - 1, points + j)

        kMaxPoint = 6
        counts = [0] * ((kMaxPoint - 1) * n + 1)
        ans = []
        for i in range(1, kMaxPoint + 1):
            Probalities(n, n, i)
        total = math.pow(kMaxPoint, n)
        for point in counts:
            ans.append(point / total)
        return ans



solution = Solution()
print(solution.dicesProbability(2))
print(solution.dicesProbability2(2))