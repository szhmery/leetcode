import math
from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1ty4y187dh
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != math.inf else -1

    # greed and DFS, pruning
    def coinChange2(self, coins: List[int], amount: int) -> int:

        self.ans = float('inf')

        # Start searching from the biggest coin
        coins.sort(reverse=True)
        self.dfs(coins, amount, 0)
        return -1 if self.ans == float('inf') else self.ans

    def dfs(self, coins, amount, prev_count):
        """
        Recursive DFS function to seach valid coins combination.
        First is to use greedy method find out a potential-best solution.
        Then start to search the second biggest coin with pruning when the coins number >= the potential-best solution.

        Args:
            coins: coins list from which we pick coins into combination
            amount: target amount
            prev_count: number of coins picked before this round

        """
        # Set up stop condtion
        if len(coins) == 0:
            return

        if amount % coins[0] == 0:
            # Update potential answer
            self.ans = min(self.ans, prev_count + amount // coins[0])
        else:
            for k in range(amount // coins[0], -1, -1):
                # Set up pruning condition
                if prev_count + k >= self.ans:
                    break
                self.dfs(coins[1:], amount - k * coins[0], prev_count + k)


if __name__ == '__main__':
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    num = solution.coinChange(coins, amount)
    print(num)
    num = solution.coinChange2(coins, amount)
    print(num)

    coins = [2]
    amount = 3
    num = solution.coinChange(coins, amount)
    print(num)
    num = solution.coinChange2(coins, amount)
    print(num)
