from typing import List


class Solution:
    #https://leetcode.com/problems/max-consecutive-ones/discuss/96712/Simple-Python
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
                count = max(count, cur)
            else:
                cur = 0

        return count

    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:

        count = 0
        cur = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == 1 and nums[i] == nums[i - 1]:
                cur += 1
                count = max(count, cur)
            elif nums[i] == 1:
                count = max(count, cur)
                cur = 1
            else:
                count = max(count, cur)
                cur = 0
        return max(count, cur)


solution = Solution()
print(solution.findMaxConsecutiveOnes([1, 1, 0, 0, 1, 1, 1]))
print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(solution.findMaxConsecutiveOnes([1, 1, 1]))
print(solution.findMaxConsecutiveOnes([1]))
print(solution.findMaxConsecutiveOnes([0]))
print(solution.findMaxConsecutiveOnes([1, 0]))
print(solution.findMaxConsecutiveOnes([0, 1]))
