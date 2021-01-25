from typing import List


class Solution:
    def maxProfit(self, prices:List[int])->int:

        sell_point = 0
        for i in range(len(prices)):
            buy = prices[i]
            if i < sell_point:
                continue
            for j in range(i,len(prices)):
                profit = 0
                if prices[j] >= buy:
                    # still increases
                    if prices[j]-buy > profit:
                        sell = prices[j]
                        profit = sell - buy
                    continue
                elif prices[j] < buy:
                    # price goes down
                    buy = prices[j]
                    i = sell_point
                    break
        max_profit = 0
        for profit in profits:
            max_profit=max_profit+profit
            print(profit)
        print("max profit:{}".format(max_profit))
        return max_profit

    def maxProfitAnswer(self,prices->List[int]) -> int:
        

if __name__=="__main__":
    solution = Solution()
    prices=[1,2,3,4,5]
    solution.maxProfit(prices)