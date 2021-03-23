from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        last_num = None
        for num in nums:
            if num == last_num:
                continue
            else:
                nums[i] = num
                i += 1
            last_num = num
        for k in range(i, len(nums)):
            nums.pop(len(nums) - 1)
        return i


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
