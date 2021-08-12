from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x, y, n, m = 0, 0, 0, 1
        for num in nums:         # 1. 遍历异或
            n ^= num
        while n & m == 0:        # 2. 循环左移，计算 m
            m <<= 1
        for num in nums:         # 3. 遍历 nums 分组
            if num & m: x ^= num # 4. 当 num & m != 0
            else: y ^= num       # 4. 当 num & m == 0
        return x, y              # 5. 返回出现一次的数字

    def singleNumbers2(self, nums: List[int]) -> List[int]:
        r = 0
        res = [0, 0]
        for num in nums:
            r ^= num
        mask = r & ~(r - 1)  # find the last 1 bit
        for num in nums:
            if mask & num:
                res[0] ^= num  # 分两组异或，就能分别找到他们
            else:
                res[1] ^= num
        return res

