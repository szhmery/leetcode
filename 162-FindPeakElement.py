from typing import List


class Solution:
    # iterative binary search
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right: # no equal
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1 # mid+1 is bigger, choose mid + 1
            else:
                right = mid # mid is bigger, choose mid
        return left

    # https://www.bilibili.com/video/BV1Rb411n7dT?from=search&seid=9512522565622787866
    def findPeakElement2(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(1, size - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
        return [0, size - 1][nums[0] < nums[size - 1]]


    # recursion binary search
    def findPeakElement3(self, nums: List[int]) -> int:
        def binary_search(nums, left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                return binary_search(nums, mid + 1, right)
            else:
                return binary_search(nums, left, mid)

        return binary_search(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    tokens = [1, 2, 3, 5, 6, 7, 8]
    result = solution.findPeakElement(tokens)
    print(result)

    tokens = [1, 2, 3, 5, 6, 7, 8]
    result = solution.findPeakElement2(tokens)
    print(result)

    tokens = [1, 2, 3, 5, 6, 7, 8]
    result = solution.findPeakElement3(tokens)
    print(result)
