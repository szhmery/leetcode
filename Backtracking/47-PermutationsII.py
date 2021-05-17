from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], Counter(nums), ans)
        return ans

    def helper(self, nums, element, counter, ans):
        if len(element) == len(nums):
            ans.append(element[::])
            return
        for num in counter:
            if counter[num] > 0:
                counter[num] -= 1
                element.append(num)
                self.helper(nums, element, counter, ans)
                element.pop()
                counter[num] += 1

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results

if __name__ == '__main__':
    solution = Solution()
    n = [1, 2, 1]
    result = solution.permuteUnique(n)
    print(result)

    result = solution.permuteUnique2(n)
    print(result)