from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 5

    result = solution.searchInsert(nums, target)
    print(result)

    nums = [1, 3, 5, 6]
    target = 2
    result = solution.searchInsert(nums, target)
    print(result)