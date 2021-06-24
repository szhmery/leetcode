from typing import List


class Solution:
    # backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n == 0:
            return ans

        def helper(first: int, curr: List[int]):
            if len(curr) == k:
                ans.append(curr[:])
                return ans
            for i in range(first, n):
                curr.append(nums[i])
                helper(i + 1, curr)
                curr.pop()

        for k in range(n + 1):
            helper(0, [])
        return ans

    # Complexity Analysis
    # https://leetcode.com/problems/subsets/solution/
    # Time complexity: O(N×2^N) to generate all subsets and then copy them into output list.
    # Space complexity: O(N×2^N). This is exactly the number of solutions for subsets multiplied by the number NN of
    # elements to keep for each subset.
    # For a given number, it could be present or absent (i.e. biolution. As nary choice) in a subset sas result,
    # for NN numbers, we would have in total 2^N
    #   choices (solutions).
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [curr + [num] for curr in ans]
        return ans

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


if __name__ == '__main__':
    solution = Solution()
    n = [1, 2, 3]
    result = solution.subsets(n)
    print(result)

    result = solution.subsets2(n)
    print(result)

    result = solution.subsets3(n)
    print(result)
