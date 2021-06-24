from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1NJ411h76f?from=search&seid=437441675472736009
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        map_dict = {}
        for i, num in enumerate(nums):
            if num in map_dict and k >= i - map_dict[num]:
                return True
            else:
                map_dict[num] = i
        return False


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,1]
    k = 3
    is_duplicate = solution.containsNearbyDuplicate(nums, k)
    print("Is duplicated: {}".format(is_duplicate))

    nums = [99,99]
    k = 2
    is_duplicate = solution.containsNearbyDuplicate(nums, k)
    print("Is duplicated: {}".format(is_duplicate))


