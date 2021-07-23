from typing import List


class Solution:
    # 1 1 2 2 3 5
    # 1^1^2^2^3^5 = 3(0011)^5(0101) = 6(0110)
    # 6(0110) & -6(1010) = 2(0010)取最右1bit
    # n ^ 2 == 0 -> 2 2 3
    # n ^ 2 != 0 -> 1 1 5
    # 3 ^ 2 ^ 2 = 5
    # 5 ^ 1 ^ 1 = 3
    # bit manipulation
    #https://leetcode.com/problems/single-number-iii/discuss/403959/python-bit
    #https://www.bilibili.com/video/BV1QK411J7dN?from=search&seid=1151504555755089353
    def singleNumber(self, nums: List[int]) -> List[int]:
        r = 0
        res = [0, 0]
        for num in nums:
            r ^= num
        mask = r & ~(r-1) #find the last 1 bit
        for num in nums:
            if mask & num:
                res[0] ^= num #分两组异或，就能分别找到他们
            else:
                res[1] ^= num
        return res

    def singleNumber2(self, nums: List[int]) -> List[int]:
        r = 0
        for num in nums:
            r ^= num

    def singleNumber2(self, nums: List[int]) -> List[int]:
        ans = set()
        for num in nums:
            if num in ans:
                ans.remove(num)
            else:
                ans.add(num)
        return list(ans)

solution = Solution()
print(solution.singleNumber([1, 1, 2, 2, 3, 5]))
print(solution.singleNumber([1,2,1,3,2,5]))
print(solution.singleNumber2([1, 1, 2, 2, 3, 5]))
print(solution.singleNumber([0, 1]))
print(solution.singleNumber2([0, 1]))