from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False

        # for i in range(len(nums)):
        #     if nums.count(nums[i]) > 1:
        #         return True
        # return False


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    is_duplicate = solution.containsDuplicate(nums)
    print("Is duplicated: {}".format(is_duplicate))

    nums = [1, 2, 3, 1]
    is_duplicate = solution.containsDuplicate(nums)
    print("Is duplicated: {}".format(is_duplicate))
