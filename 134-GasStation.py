from functools import reduce
from typing import List


class Solution:
    # https://www.bilibili.com/video/BV13k4y1o7SU?from=search&seid=6423544724850199962
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = reduce(lambda x, y: x + y, gas)
        total_cost = reduce(lambda x, y: x + y, cost)
        if total_gas < total_cost:
            return -1
        current_gas = 0
        start = 0
        for i in range(len(gas)):
            current_gas = current_gas + gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start = i + 1

        return start


if __name__ == '__main__':
    solution = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    result = solution.canCompleteCircuit(gas, cost)
    print(result)
