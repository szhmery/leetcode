from typing import List


class Solution:
    # two pointers
    # https://www.bilibili.com/video/BV1ba4y1t7eK
    def moveZeroes(self, nums: List[int]) -> None:
        l, r, n = 0, 0, len(nums)
        while r < n:
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            r += 1
        while l < n:
            nums[l] = 0
            l += 1


    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 0, 4, 5, 6, 0, 1]
    print("Before move zeroes:{}".format(nums))
    solution.moveZeroes(nums)
    print("after move zeroes:{}".format(nums))
    solution.moveZeroes2(nums)
    print("after move zeroes:{}".format(nums))
