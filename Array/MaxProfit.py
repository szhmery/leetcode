from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next_buy_point = 0
        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            profit = 0
            sell = 0
            if i < next_buy_point:
                continue
            for j in range(i + 1, len(prices)):
                if prices[j] >= buy and prices[j] > sell:
                    sell = prices[j]
                else:
                    if sell > buy:
                        profit = sell - buy
                        max_profit = max_profit + profit
                        print("Sell at {0}, buy at {1}, profit {2}".format(sell, buy, profit))
                    buy = prices[j]
                    sell = 0
                    next_buy_point = j
                    break
                if j == len(prices) - 1 and sell != 0:
                    if sell > buy:
                        profit = sell - buy
                        max_profit = max_profit + profit
                        print("Sell at {0}, buy at {1}, profit {2}".format(sell, buy, profit))
                        return max_profit
                continue
        return max_profit

    def maxProfitAnswer(self, prices: List[int]) -> int:
        vally = prices[0]
        peak = prices[0]
        max_profit = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            vally = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit = max_profit + peak - vally

        return max_profit


if __name__ == "__main__":
    solution = Solution()
    prices1 = [1, 2, 3, 4, 5]
    max = solution.maxProfit(prices1)
    max_answer = solution.maxProfitAnswer(prices1)
    print("max profit {0} : {1}".format(max, max_answer))
    prices2 = [7, 1, 5, 3, 6, 4]
    max = solution.maxProfit(prices2)
    max_answer = solution.maxProfitAnswer(prices2)
    print("max profit {0} : {1}".format(max, max_answer))
    prices3 = [7, 6, 4, 3, 1]
    max = solution.maxProfit(prices3)
    max_answer = solution.maxProfitAnswer(prices3)
    print("max profit {0} : {1}".format(max, max_answer))
    prices4 = [2, 1, 4, 5, 2, 9, 7]
    max = solution.maxProfit(prices4)
    max_answer = solution.maxProfitAnswer(prices4)
    print("max profit {0} : {1}".format(max, max_answer))
