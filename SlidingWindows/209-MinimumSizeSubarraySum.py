from typing import List
from bisect import bisect_left

class Solution:
    # two pointers/ sliding windows
    # Time complexity: O(n)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        ans = float('inf')
        n = len(nums)
        left = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            while sum >= target:
                ans = min(ans, i + 1 - left)
                sum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0

    # binary search
    # Time complexity: O(nlog(n))
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sum = [0] * (n + 1)
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + nums[i - 1]
        ans = n + 1
        for i in range(n):
            l = i
            r = n
            while l <= r:
                mid = l + (r - l) // 2
                if sum[mid] - sum[i] >= target:
                    ans = min(ans, mid - i)
                    r = mid - 1
                else:
                    l = mid + 1

        return ans if ans != n + 1 else 0


    def minSubArrayLen3(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        n = len(nums)
        for i in range(n):
            j = i
            cur_sum = 0
            while j < n:
                cur_sum += nums[j]
                if cur_sum >= target:
                    ans = min(ans, j - i + 1)
                    break
                j += 1

        return ans if ans != float('inf') else 0


if __name__ == "__main__":
    solution = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = solution.minSubArrayLen(target, nums)
    print(result)
    result = solution.minSubArrayLen2(target, nums)
    print(result)
    target = 4
    nums = [1, 4, 4]
    result = solution.minSubArrayLen(target, nums)
    print(result)
    result = solution.minSubArrayLen2(target, nums)
    print(result)

