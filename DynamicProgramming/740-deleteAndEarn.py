from typing import List


class Solution:
    # 时间复杂度：O(N+M)，其中 N 是数组 nums 的长度，M 是 nums 中元素的最大值。
    # 空间复杂度：O(M)。
    # https://leetcode-cn.com/problems/delete-and-earn/solution/ru-guo-ni-li-jie-liao-da-jia-jie-she-zhe-ti-ni-ken/
    def deleteAndEarn(self, nums: List[int]) -> int:
        def rob(nums):
            pre, cur = 0, 0
            for i in range(len(nums)):
                pre, cur = cur, max(cur, pre + i * nums[i])
            return cur

        idx = [0] * (max(nums) + 1)
        for i in range(len(nums)):
            idx[nums[i]] += 1
        return rob(idx)

so = Solution()
print(so.deleteAndEarn(nums = [3,4,2]))
print(so.deleteAndEarn(nums = [2,2,3,3,3,4]))