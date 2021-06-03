import math


class Solution:
    # https://www.bilibili.com/video/BV1r5411Y7MH
    # DP
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(math.sqrt(n) + 1))]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for square in squares:
                if i < square:
                    continue
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]

    # https://www.bilibili.com/video/BV1r5411Y7MH
    # BFS
    def numSquares2(self, n: int) -> int:
        squares = [i * i for i in range(1, int(math.sqrt(n) + 1))]
        level = 0
        queue = {n}
        while queue:
            level += 1
            tmp = set()
            for num in queue:
                for square in squares:
                    if num == square:
                        return level
                    elif num < square:
                        break
                    else:
                        tmp.add(num - square)
            queue = tmp


if __name__ == "__main__":
    solution = Solution()
    result = solution.numSquares(12)
    print(result)
    result = solution.numSquares(13)
    print(result)
    result = solution.numSquares2(12)
    print(result)
    result = solution.numSquares2(13)
    print(result)


