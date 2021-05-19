from typing import List
import math


class Solution:
    # brute force
    # Complexity Analysis
    # Time complexity : O(2^n). Size of recursion tree will be 2^n
    # Space complexity : O(n^2). memo array of size n∗n is used.
    # time limit exceed
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.sub_lengthOfLIS(nums, float('-inf'), 0)

    def sub_lengthOfLIS(self, nums, prev, curpos):
        if curpos == len(nums):
            return 0
        taken = 0
        if nums[curpos] > prev:
            taken = 1 + self.sub_lengthOfLIS(nums, nums[curpos], curpos + 1)
        untaken = self.sub_lengthOfLIS(nums, prev, curpos + 1)
        return max(taken, untaken)
    # DP
    # Complexity Analysis
    # Time complexity : O(n^2)  Two loops of n are there.
    # Space complexity : O(n). dp array of size n is used.
    def lengthOfLIS2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        maxans = 1
        for i in range(1, len(nums)):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
        return maxans


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    num = solution.lengthOfLIS(nums)
    print(num)
    num = solution.lengthOfLIS2(nums)
    print(num)
    nums = [0,1,0,3,2,3]
    num = solution.lengthOfLIS(nums)
    print(num)
    num = solution.lengthOfLIS2(nums)
    print(num)
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    num = solution.lengthOfLIS(nums)
    print(num)
    num = solution.lengthOfLIS2(nums)
    print(num)