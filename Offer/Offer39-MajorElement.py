from typing import List
class Solution:
    # 时间复杂度 O(N) ： N 为数组 nums 长度。
    # 空间复杂度 O(1) ： votes 变量使用常数大小的额外空间
    # 摩尔投票
    # 每轮假设发生 票数和 =0 都可以 缩小剩余数组区间 。当遍历完成时，最后一轮假设的数字即为众数。
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x

    # 加入验证。
    def majorityElement2(self, nums: List[int]) -> int:
        votes, count = 0, 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        # 验证 x 是否为众数
        for num in nums:
            if num == x: count += 1
        return x if count > len(nums) // 2 else 0 # 当无众数时返回 0
