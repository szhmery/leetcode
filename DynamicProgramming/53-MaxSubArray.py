import math
from typing import List


class Solution:
    # Complexity Analysis
    # Time complexity: O(N), where N is the length of nums.
    # We iterate through every element of nums exactly once.
    # Space complexity: O(1)
    # No matter how long the input is, we are only ever using 2 variables: currentSubarray and maxSubarray.
    # https://www.bilibili.com/video/BV11A41187AR?from=search&seid=3304823974143982280
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = current_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray

    # DP
    def maxSubArray2(self, nums: List[int]) -> int:
        memo = [None] * len(nums)
        memo[0] = nums[0]
        max_count = nums[0]
        for i in range(1, len(nums)):
            memo[i] = max(nums[i], memo[i-1] + nums[i])
            max_count = max(max_count, memo[i])
        return max_count

    # Complexity Analysis
    # Time complexity: O(N⋅logN), where N is the length of nums.
    # Space complexity: O(logN), where N is the length of nums.
    def maxSubArray4(self, numbs: List[int]) -> int:

        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)

        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)

    """
    # Complexity Analysis
    # Time complexity: O(N^2), where NN is the length of nums.
    # We use 2 nested for loops, with each loop iterating through nums.
    # Space complexity: O(1)
    # No matter how big the input is, we are only ever using 2 variables: ans and currentSubarray.
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        return max_subarray
    """

if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.maxSubArray(nums)
    print('Max Sub Array:{}'.format(result))
    result = solution.maxSubArray2(nums)
    print('Max Sub Array:{}'.format(result))
    result = solution.maxSubArray3(nums)
    print('Max Sub Array:{}'.format(result))
    result = solution.maxSubArray4(nums)
    print('Max Sub Array:{}'.format(result))
