from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1Hv411B7rd?from=search&seid=10771394802532231330
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1 == 1:
                    count += 1 #找出位數全部为1的个数
            res |= (count % 3) << i #把不是3的倍数的位找出来相加，就是剩下的那一个
        return res - 2 ** 31 if (res >> 31) & 1 else res

    def singleNumber2(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2


solution = Solution()
print(solution.singleNumber([1, 1, 2, 2, 2, 1, 3]))
print(solution.singleNumber2([1, 1, 2, 2, 2, 1, 3]))
print(solution.singleNumber([2147483647, 1, 1, 1]))
print(solution.singleNumber2([2147483647, 1, 1, 1]))
