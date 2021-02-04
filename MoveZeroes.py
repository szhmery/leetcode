from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)

if __name__ == "__main__":
    solution = Solution()
    nums = [1,0,4,5,6,0,1]
    print("Before move zeroes:{}".format(nums))
    solution.moveZeroes(nums)
    print("after move zeroes:{}".format(nums))

