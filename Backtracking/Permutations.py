from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], ans)
        return ans

    def helper(self, nums, element, result):
        if len(element) == len(nums):
            result.append(element[:])
            return result
        for num in nums:
            if num in element:
                continue
            else:
                element.append(num)
                self.helper(nums, element, result)
                element.pop()


if __name__ == '__main__':
    solution = Solution()
    n = [1, 2, 3]
    result = solution.permute(n)
    print(result)
