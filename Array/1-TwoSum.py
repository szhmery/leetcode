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

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums_dict.keys() and i != nums_dict[another]:
                return [i, nums_dict[another]]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums_dict.keys():
                return [nums_dict[another], i]
            else:
                nums_dict.update({nums[i]: i})


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print("nums {0}, method 1: target {1}, indices {2}".format(nums, target, result))
    result = solution.twoSum2(nums, target)
    print("nums {0}, method 2: target {1}, indices {2}".format(nums, target, result))
    result = solution.twoSum3(nums, target)
    print("nums {0}, method 3: target {1}, indices {2}".format(nums, target, result))

    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    print("nums {0}, method 1: target {1}, indices {2}".format(nums, target, result))
    result = solution.twoSum2(nums, target)
    print("nums {0}, method 2: target {1}, indices {2}".format(nums, target, result))
    result = solution.twoSum3(nums, target)
    print("nums {0}, method 3: target {1}, indices {2}".format(nums, target, result))

    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print("nums {0}, method 1: target {1}, indices {2}".format(nums, target, result))
    result = solution.twoSum2(nums, target)
    print("nums {0}, method 2: target {1}, indices {2}".format(nums, target, result))
    result = solution.twoSum3(nums, target)
    print("nums {0}, method 3: target {1}, indices {2}".format(nums, target, result))
