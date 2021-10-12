from typing import List


class Solution:
    # greedy
    def canJump(self, nums: List[int]) -> bool:
        max_steps = 0
        for i in range(len(nums) - 1):
            max_steps = max(max_steps, i + nums[i])
            if max_steps < i + 1:  # 如果这次的最大步数不能达到下一个台阶，那么就是false
                return False
        return True

    def canJump2(self, nums: List[int]) -> bool:
        max_steps = 0
        for i in range(len(nums)):
            if max_steps < i:  # 如果最大步数不能到达这个台阶，那么失败。
                return False
            max_steps = max(max_steps, i + nums[i])  # 计算下个最大步数

        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.canJump([3, 2, 1, 0, 4])
    print(result)

    result = solution.canJump([2, 3, 1, 1, 4])
    print(result)
