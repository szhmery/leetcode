from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_list = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result_list.append(i)
                    result_list.append(j)
                    return result_list

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print("nums {0}, target {1}, indices {2}".format(nums, target, result))
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    print("nums {0}, target {1}, indices {2}".format(nums, target, result))

    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print("nums {0}, target {1}, indices {2}".format(nums, target, result))

