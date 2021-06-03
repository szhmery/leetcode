from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = []
        l = len(nums)
        for i in range(l):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] == i - k:
                queue.pop(0)
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print("Before move zeroes:{}".format(nums))
    result = solution.maxSlidingWindow(nums, k)
    print("method 1:{}".format(result))
