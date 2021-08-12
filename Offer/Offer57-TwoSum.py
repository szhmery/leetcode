from typing import List


class Solution:
    #时间复杂度 O(N) ： NN 为数组 nums 的长度；双指针共同线性遍历整个数组。
    #空间复杂度 O(1) ： 变量 i, j 使用常数大小的额外空间。
    # two pointers, sorted array.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]
        return []
