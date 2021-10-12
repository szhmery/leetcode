import sys
from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1K4411Z7Gd?from=search&seid=3314387864695428406
    def jump(self, nums: List[int]) -> int:
        step = 0
        start = 0
        end = 0
        for i in range(len(nums) - 1): # 不需要在最后一个格子跳，所以不用到最后一个格子
            end = max(end, i + nums[i]) # 能到达的最右格子
            if i == start: # 如果达到了下个区域的左界限
                step += 1 # 步数增加一个，因为区域增加一个
                start = end # 更新右界限
        return step

    # DP
    # https://www.bilibili.com/video/BV1854y1x7cH?from=search&seid=3314387864695428406
    # BFS is not implemented
    def jump2(self, nums: List[int]) -> int:
        dp = [sys.maxsize] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i):
                if i - j <= nums[j]:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[len(nums) - 1]


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    result = solution.jump(nums)
    print(result)
    result = solution.jump2(nums)
    print(result)
