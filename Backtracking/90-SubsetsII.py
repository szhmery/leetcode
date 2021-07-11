from typing import List


class Solution:
    # https://leetcode.com/problems/subsets-ii/solution/
    # iterative
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        subsets = [[]]
        set_size = 0
        for i in range(n):
            if i >= 0 and nums[i] == nums[i - 1]:
                start_index = set_size
            else:
                start_index = 0
            set_size = len(subsets)
            for j in range(start_index, len(subsets)):
                cur_subset = subsets[j][:]  # copy one array of subsets
                cur_subset.append(nums[i])
                subsets.append(cur_subset)
        return subsets

    # backtracking
    # Time complexity:O(N×2^N)
    # Space complexity: O(N)
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        def helper(index, curr, ans):
            ans.append(curr[:])
            for i in range(index, len(nums)):
                if i > index and nums[i - 1] == nums[i]:
                    continue
                curr.append(nums[i])
                helper(i + 1, curr, ans)  # increase i, not index
                curr.pop()

        nums.sort()
        n = len(nums)
        if n == 0:
            return []
        ans = []
        helper(0, [], ans)
        return ans

    # bit manipulation
    # Time complexity:O(N×2^N)
    # Space complexity: O(N×2^N)
    def subsetsWithDup3(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []
        nth_set = 1 << n
        nums.sort()
        ans = []
        for i in range(2 ** n):
            bitmask = bin(i | nth_set)[3:]  # remove 0xb
            curr = []
            for j in range(n):
                if bitmask[j] == '1':
                    curr.append(nums[j])

            if curr not in ans:
                ans.append(curr)

        return ans

    def subsetsWithDup4(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n == 0:
            return res

        def hepler(first, curr):
            if len(curr) == k:
                if sorted(curr) not in res:
                    res.append(sorted(curr[:]))
                return res
            for i in range(first, n):
                curr.append(nums[i])
                hepler(i + 1, curr)
                curr.pop()

        for k in range(n + 1):
            hepler(0, [])
        return res


solution = Solution()
print(solution.subsetsWithDup([1, 2, 2, 3]))
print(solution.subsetsWithDup([4, 4, 4, 1, 4]))
print(solution.subsetsWithDup2([1, 2, 2, 3]))
print(solution.subsetsWithDup2([4, 4, 4, 1, 4]))
print(solution.subsetsWithDup3([1, 2, 2, 3]))
print(solution.subsetsWithDup3([4, 4, 4, 1, 4]))
print(solution.subsetsWithDup4([1, 2, 2, 3]))
print(solution.subsetsWithDup4([4, 4, 4, 1, 4]))
