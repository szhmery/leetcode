from typing import List
from collections import Counter


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], ans)
        return ans

    def helper(self, nums, element, ans):
        if len(element) == len(nums):
            ans.append(element[::])
            return
        for num in nums:
            if num in element:
                continue
            element.append(num)
            self.helper(nums, element, ans)
            element.pop()


if __name__ == '__main__':
    solution = Solution()
    n = [1, 2, 3]
    result = solution.permute(n)
    print(result)
