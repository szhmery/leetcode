from typing import List


class Solution:
    #https://www.bilibili.com/video/BV1pB4y1A747?from=search&seid=8098118433140481209
    # n = len(nums)
    # m ——> times
    # n * x = sum + m(n-1)
    # x = min + m
    # n *(min + m) = sum + m(n-1)
    # n * min = sum -m
    # m = sum - n * min
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(nums) - n * min(nums)
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        steps = 0
        n = len(nums)
        maxinum = -float('inf')
        while True:
            same_count = 0
            for i in range(n):
                if i < n - 1 and nums[i] == nums[i + 1]:
                    same_count += 1
                if same_count == n - 1 and i == n - 1:
                    return steps
            for i in range(n):
                if nums[i] > maxinum:
                    m = i
                    maxinum = nums[i]
                nums[i] += 1
            nums[m] -= 1
            steps += 1

solution = Solution()
print(solution.minMoves([1, 2, 3]))
print(solution.minMoves([1, 1, 1]))