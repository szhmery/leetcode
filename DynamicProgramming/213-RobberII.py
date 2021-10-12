from typing import List


class Solution:
    # 时间复杂度：O(n)，其中 n 是数组长度。需要对数组遍历两次，计算可以偷窃到的最高总金额。
    # 空间复杂度：O(1)。
    # https://leetcode-cn.com/problems/house-robber-ii/solution/213-da-jia-jie-she-iidong-tai-gui-hua-jie-gou-hua-/
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]

    def rob(self, nums: List[int]) -> int:
        def helper(homes):
            if len(homes) == 1:
                return homes[0]
            pre = homes[0]
            cur = max(homes[0], homes[1])
            for i in range(2, len(homes)):
                pre, cur = cur, max(cur, pre + homes[i])
            return cur

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        return max(helper(nums[1:]), helper(nums[:-1]))


So = Solution()
print(So.rob(nums=[2, 3, 2]))
print(So.rob([1, 2, 3, 1]))
