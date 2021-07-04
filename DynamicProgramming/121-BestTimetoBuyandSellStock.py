import math
from typing import List


class Solution:
    # DP
    # Complexity Analysis
    # Time complexity : O(n). Only a single pass is needed.
    # Space complexity : O(1). Only two variables are used.
    def maxProfit(self, prices: List[int]) -> int:
        # min_price = math.pow(10, 4)
        min_price = math.inf
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                if prices[i] - min_price > max_profit:
                    max_profit = prices[i] - min_price
        return max_profit

    # dp
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])

            dp[i] = max(dp[i - 1] , prices[i]-min_price)
        return dp[-1]

    """
    # Time complexity : O(n^2). Loop runs (n-1)*n/2 times.
    # Space complexity : O(1)O(1). Only two variables - max_profit and profit are used.
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                if profit >= max_profit:
                    max_profit = profit
        return max_profit
    """


if __name__ == "__main__":
    solution = Solution()
    prices1 = [1, 2, 3, 4, 5]
    result = solution.maxProfit2(prices1)
    print("max profit {0}".format(result))

    prices = [7, 6, 4, 3, 1]
    result = solution.maxProfit2(prices)
    print("max profit {0}".format(result))
