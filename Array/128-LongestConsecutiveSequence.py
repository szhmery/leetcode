from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        ans = 1
        nums.insert(0, float('inf'))
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    cur_len += 1
                    ans = max(ans, cur_len)
                else:
                    cur_len = 1
        return ans

    def longestConsecutive2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        ans = 1

        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in num_set:
                    cur_len += 1
                    cur_num += 1
                    ans = max(cur_len, ans)
        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result = solution.longestConsecutive(nums)
    print(result)
    result = solution.longestConsecutive(nums)
    print(result)
    nums = [100, 4, 200, 1, 3, 2]
    result = solution.longestConsecutive(nums)
    print(result)
    result = solution.longestConsecutive(nums)
    print(result)
    nums = [0, 2, 1, 1]
    result = solution.longestConsecutive(nums)
    print(result)
    result = solution.longestConsecutive(nums)
    print(result)