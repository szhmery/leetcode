from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1N541177Bk?from=search&seid=1830710312737531822
    # Using Reverse
    # Time complexity: O(n).
    # Space complexity: O(1).
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, lo, hi):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        if len(nums) == 1:
            return
        n = len(nums)
        k %= n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

    # https://leetcode.com/problems/rotate-array/solution/
    def rotate4(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            # nums = [nums.pop()]+ nums
            nums.insert(0, nums.pop())

    # brute force
    # Time complexity: O(n×k).
    # Space complexity: O(1).
    def rotate1(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]

    # extra array
    # Time complexity: O(n).
    # Space complexity: O(n).
    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        nums[:] = a

    # Using Cyclic Replacements
    # Time complexity: O(n).
    # Space complexity: O(1).
    def rotate3(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1




if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    print("before rotate:{}".format(nums))
    solution.rotate(nums, 2)
    print("after rotate:{}".format(nums))
    nums = [1, 2, 3, 4, 5]
    solution.rotate4(nums, 2)
    print("after rotate:{}".format(nums))
