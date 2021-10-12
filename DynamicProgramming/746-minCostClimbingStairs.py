from typing import List


class Solution:
    #https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/yi-bu-yi-bu-tui-dao-dong-tai-gui-hua-de-duo-chong-/
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        dp = [0] * (len(cost))

        dp[0] = 0
        dp[1] = min(cost[0], cost[1])

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i - 1])

        return dp[-1]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        minCost0, minCost1 = 0, min(cost[0], cost[1])
        mincost = minCost1
        for i in range(2, len(cost)):
            mincost = min(minCost0 + cost[i - 1], minCost1 + cost[i])
            minCost0, minCost1 = minCost1, mincost
        return mincost


so = Solution()
print(so.minCostClimbingStairs(cost = [10, 15, 20]))
print(so.minCostClimbingStairs2(cost = [10, 15, 20]))