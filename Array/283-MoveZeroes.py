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

    # 时间复杂度：O(n)，其中 n 为序列长度。每个位置至多被遍历两次。
    # 空间复杂度：O(1)。只需要常数的空间存放若干变量。

    def moveZeroes2(self, nums: List[int]) -> None:
        l, r, n = 0, 0, len(nums)
        while r < n:  # 左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]  # 每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变。
                l += 1
            r += 1
        return

    def moveZeroes3(self, nums: List[int]) -> None:
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
