from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[len(nums) - 1]

    def rob2(self, nums: List[int]) -> int:
        cur_max = pre_max = 0

        for i in range(len(nums)):
            tmp = cur_max
            cur_max = max(cur_max, nums[i] + pre_max)
            pre_max = tmp
        return cur_max

    def rob3(self, nums: List[int]) -> int:
        a = b = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                a = max(a + nums[i], b)
            else:
                b = max(b + nums[i], a)
        return max(a, b)


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    result = solution.rob(nums)
    print('Max rob:{}'.format(result))
    nums = [2, 1, 1, 2]
    result = solution.rob(nums)
    print('Max rob:{}'.format(result))

    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    result = solution.rob2(nums)
    print('Max rob:{}'.format(result))
    nums = [2, 1, 1, 2]
    result = solution.rob2(nums)
    print('Max rob:{}'.format(result))

    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    result = solution.rob3(nums)
    print('Max rob:{}'.format(result))
    nums = [2, 1, 1, 2]
    result = solution.rob3(nums)
    print('Max rob:{}'.format(result))
