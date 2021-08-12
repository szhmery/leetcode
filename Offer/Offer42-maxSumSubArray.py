from typing import List
import math
class Solution:
    #DP
    #间复杂度 O(N) ： 线性遍历数组 nums 即可获得结果，使用 O(N) 时间。
    #空间复杂度 O(1) ： 使用常数大小的额外空间。
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums and len(nums) == 0:
            return
        cur_sum = 0
        mx = -math.inf
        for i in range(len(nums)):
            if cur_sum < 0: #如果前面的sum小于0，那么还是用nums[i],不要增加该sum
                cur_sum = nums[i]
            else:#如果前面的sum大于0，在加上nums[i]
                cur_sum += nums[i]
            if cur_sum > mx:#并取出最大的那个值
                mx = cur_sum
        return mx
    #nums用来做动态规划的数组，如果nums[i-1] <0 就选用nums[i]
    def maxSubArray2(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

