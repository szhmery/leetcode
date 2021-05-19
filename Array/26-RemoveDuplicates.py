from typing import List


class Solution:
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/

    # two pointers
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(i, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1




if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    print("Before:")
    print(nums)
    print("After:")
    print(solution.removeDuplicates(nums))
    print(nums)

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("Before:")
    print(nums)
    print("After:")
    print(solution.removeDuplicates(nums))
    print(nums)
