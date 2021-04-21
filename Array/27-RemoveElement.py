from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        if nums is None:
            return 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    print("Before:")
    print(nums)
    print("After:")
    print(solution.removeElement(nums, 2))
    print(nums)