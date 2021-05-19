from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_steps = 0
        for i in range(len(nums) - 1):
            max_steps = max(max_steps, i + nums[i])
            if max_steps < i + 1:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.canJump([3, 2, 1, 0, 4])
    print(result)

    result = solution.canJump([2, 3, 1, 1, 4])
    print(result)
