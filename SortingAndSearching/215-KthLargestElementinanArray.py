import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        for i in range(0, len(nums)):

            k -= 1
            if k == 0:
                return nums[i]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        target = len(nums) - k
        cur = -1
        while cur != target:
            cur = self.quick_sort(nums, left, right)
            if cur < target:
                left = cur + 1
            elif cur > target:
                right = cur - 1
        return nums[cur]

    # https://www.bilibili.com/video/BV15Z4y1p7KR?t=895
    def quick_sort(self, nums, low, high):
        if low == high:
            return low
        pivot_index = low + random.randrange(high - low + 1)
        pivot = nums[pivot_index]
        nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
        i = low
        j = high - 1
        while i < j:
            while i < j and nums[i] <= pivot:
                i += 1
            while i < j and nums[j] > pivot:
                j -= 1

            if i != j:
                nums[j], nums[i] = nums[i], nums[j]
        if nums[i] > pivot:
            nums[i], nums[high] = nums[high], nums[i]
            return i

        return high


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = solution.findKthLargest2(nums, k)
    print(result)

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = solution.findKthLargest2(nums, k)
    print(result)
