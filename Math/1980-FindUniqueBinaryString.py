from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ''
        for i, num in enumerate(nums):
            ans += '1' if num[i] == '0' else '0'
        return ans
    # 时间复杂度：O(n^2)，其中 n 为nums 的长度。预处理哈希集合的时间复杂度为 O(n^2)，
    # 寻找第一个不在哈希表中的整数与生成答案字符串的时间复杂度为 O(n)。
    # 空间复杂度：O(n)，即为哈希集合的空间复杂度。

    def findDifferentBinaryString2(self, nums: List[str]) -> str:
        n = len(nums[0]) # n unique binary string, each of length is n
        # 预处理对应整数的哈希集合
        vals = {int(num, 2) for num in nums}
        # 寻找第一个不在哈希集合中的整数
        val = 0
        while val in vals:
            val += 1
        # 将整数转化为二进制字符串返回
        res = "{:b}".format(val)
        return '0' * (n - len(res)) + res

    # My method
    def findDifferentBinaryString3(self, nums: List[str]) -> str:
        if not nums:
            return
        n = len(nums[0])

        for i in range(2 ** n):
            tmp = '0' * (n - len(bin(i)[2:])) + bin(i)[2:]
            if tmp not in nums:
                return tmp
So = Solution()
print(So.findDifferentBinaryString(['111','100','101']))
print(So.findDifferentBinaryString2(['111','100','101']))
print(So.findDifferentBinaryString3(['111','100','101']))