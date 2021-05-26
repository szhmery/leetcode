from typing import List
import math


class Solution:
    # https://www.bilibili.com/video/BV1ty4y187dh
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != math.inf else -1


if __name__ == '__main__':
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    num = solution.coinChange(coins, amount)
    print(num)

    coins = [2]
    amount = 3
    num = solution.coinChange(coins, amount)
    print(num)