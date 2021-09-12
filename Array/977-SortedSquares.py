from typing import List


class Solution:
    # two pointers
    #时间复杂度：O(n)，其中 nn 是数组 nums 的长度。
    #空间复杂度：O(1)。除了存储答案的数组以外，我们只需要维护常量空间。

    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        n = len(nums)
        ans = [0] * n
        lo, hi, pos = 0, n - 1, n - 1
        while lo <= hi:
            if nums[lo] * nums[lo] > nums[hi] * nums[hi]:
                ans[pos] = nums[lo] * nums[lo]
                lo += 1
            else:
                ans[pos] = nums[hi] * nums[hi]
                hi -= 1
            pos -= 1
        return ans


so = Solution()
print(so.sortedSquares([-4, -1, 0, 3, 10]))
print(so.sortedSquares([-7, -3, 2, 3, 11]))
