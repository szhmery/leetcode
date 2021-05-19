from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        # 前缀和
        self.nums = nums
        self.pre_sum = [0]
        pre = 0
        for num in nums:
            pre += num
            self.pre_sum.append(pre)

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,2)
print(param_1)
