from typing import List


class Solution:
    #https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/344583/Python%3A-O(1)-space-solution
    # time complexity: O(N)
    # space complextiy: O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        # ans = []
        # for i in range(n):
        #     if nums[i] > 0:
        #         ans.append(i + 1)
        # return ans
        return [i + 1 for i in range(n) if nums[i] > 0]
    # time complexity: O(N)
    # space complextiy: O(N)
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        exist = set(nums)
        for i in range(1, n + 1):
            if i not in exist:
                ans.append(i)
        return ans


solution = Solution()
print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
