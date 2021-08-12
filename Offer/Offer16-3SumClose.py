from typing import List


class Solution:
    # sort and two points
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total == target:
                    return target
                if abs(target - total) < abs(target - ans):
                    ans = total
                if total > target:
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi + 1]: # if value is same with previous one, previous is hi + 1
                        hi -= 1
                elif total < target:
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo - 1]: # previous is lo - 1
                        lo += 1
        return ans

so = Solution()
print(so.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(so.threeSumClosest(nums = [-1,0,1,1,55], target = 3))
