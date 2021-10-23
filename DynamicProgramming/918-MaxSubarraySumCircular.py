from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mx, mi, cur1, cur2 = nums[0], nums[0], 0, 0
        total = 0
        for num in nums:
            total += num
            cur1 = max(num, cur1 + num)
            mx = max(cur1, mx)  # find sum of the max sub array
            cur2 = min(num, cur2 + num)
            mi = min(cur2, mi)  # find sum of the min sub array
        if mx < 0:  # if all of nums are negative
            return mx  # return the sum of max sub array
        # 情况一 最大子序列和位于中间位置，情况二 最大子序列和位于两边，然后总和减去最小和。
        return max(total - mi, mx)  # 取两者最大值


so = Solution()
print(so.maxSubarraySumCircular([1, -2, 3, -2]))
print(so.maxSubarraySumCircular([5, -3, 5]))
print(so.maxSubarraySumCircular([3, -1, 2, -1]))
print(so.maxSubarraySumCircular([-5, 3, 5]))
