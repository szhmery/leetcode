from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.lower_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

    def lower_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def higher_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    def searchRange2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]



if __name__ == "__main__":
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    result = solution.searchRange(nums, target)
    print(result)
    result = solution.searchRange2(nums, target)
    print(result)

    nums = [1, 2, 5]
    target = 4
    result = solution.searchRange(nums, target)
    print(result)
    result = solution.searchRange2(nums, target)
    print(result)
