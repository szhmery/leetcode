from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            # nums = [nums.pop()]+ nums
            nums.insert(0,nums.pop())


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    print("before rotate:{}".format(nums))
    solution.rotate(nums, 2)
    print("after rotate:{}".format(nums))
