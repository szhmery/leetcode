from typing import List


class Solution:
    # binary search
    #时间复杂度：O(logn)，其中 n 为数组的长度。二分查找所需的时间复杂度为 O(logn)。
    #空间复杂度：O(1)。我们只需要常数空间存放若干变量。
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right: # use =, return left, because left has already plus 1
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