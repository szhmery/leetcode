from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        # 把所有数的所有位数都各自相加
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m # 以3取模，3的倍数的都等于0，取消掉。剩下的就是唯一的那个数。恢复第 i 位的值到 res
        # python可以处理大数，为了防止越界，如果32位为1就是一个负数。 截取低32位，不管其他高位。
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)


