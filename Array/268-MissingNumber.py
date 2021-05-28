from typing import List


class Solution:
    # https://leetcode.com/problems/missing-number/solution/
    # hash table
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in nums:
                return i

    # Gauss' Formula
    def missingNumber2(self, nums: List[int]) -> int:
        expect_sum = (len(nums) * (len(nums) + 1)) // 2
        actual_sum = sum(nums)
        return expect_sum - actual_sum

    # Bit Manipulation
    def missingNumber3(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    # sorting
    def missingNumber4(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if nums[i] != expected_num:
                return expected_num


if __name__ == "__main__":
    solution = Solution()
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print("Before move zeroes:{}".format(nums))
    result = solution.missingNumber(nums)
    print("method 1:{}".format(result))
    result = solution.missingNumber2(nums)
    print("method 2:{}".format(result))
    result = solution.missingNumber3(nums)
    print("method 3:{}".format(result))
