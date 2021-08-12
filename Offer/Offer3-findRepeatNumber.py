from typing import List


class Solution:
    # swap
    #https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/jian-zhi-offer-mian-shi-ti-jing-xuan-tu-jie-03-shu/
    def findRepeatNumber(self, nums: List[int]) -> int:
        if not nums:
            return -1
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: #索引 nums[i] 处的值也为 nums[i]，即找到一组相同值，返回 nums[i] 即可
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            i += 1
        return -1
    def findRepeatNumber2(self, nums: List[int]) -> int:
        if not nums:
            return
        seen = set()
        for num in nums:
            if num in seen:
                break
            else:
                seen.add(num)
        return num

solution = Solution()
print(solution.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))