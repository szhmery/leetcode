from typing import List


class Solution:
    # two points
    # Time Complexity: O(n^2). We have outer and inner loops, each going through nn elements.
    # Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n^2).
    # This is asymptotically equivalent to O(n^2)
    # Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm.
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                return target
        return target - diff
    #     Binary Search


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    result = solution.threeSumClosest(nums, target)
    print(result)