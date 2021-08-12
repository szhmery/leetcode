from typing import List

#顺子，大小王是万能牌
class Solution:
    # 0 is 大王 or 小王
    # set
    def is_straight(self, nums: List) -> bool:
        exist = set()
        max_num = -1
        min_num = 14
        for num in nums:
            if num == 0:
                continue
            if num in exist:
                return False
            exist.add(num)
            max_num = max(max_num, num)
            min_num = min(min_num, num)
        return max_num - min_num < 5

    # sort
    def is_straight2(self, nums: List) -> bool:
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[joker] < 5

    # from the offer book
    def is_straight3(self, nums: List) -> bool:
        if len(nums) < 1 or len(nums) > 5:
            return False
        nums.sort() # O(nlogn)
        i = 0
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                break
        s = count_zero # the same with index of unzero number
        b = count_zero + 1
        gap = 0
        while b < 5:
            if nums[b] == nums[s]:
                return False
            gap += nums[b] - nums[s] - 1
            s = b
            b += 1
        return False if gap > count_zero else True



solution = Solution()
nums = [0, 0, 1, 2, 5]
nums = [0, 0, 1, 2, 6]
print(solution.is_straight([0, 0, 1, 2, 6]))
print(solution.is_straight2([0, 0, 1, 2, 6]))
print(solution.is_straight3([0, 0, 1, 2, 6]))
print(solution.is_straight([0, 0, 1, 2, 5]))
print(solution.is_straight2([0, 0, 1, 2, 5]))
print(solution.is_straight3([0, 0, 1, 2, 5]))

print(solution.is_straight([0, 4, 1, 2, 2]))
print(solution.is_straight2([0, 4, 1, 2, 2]))
print(solution.is_straight3([0, 4, 1, 2, 2]))
print(solution.is_straight([1, 4, 5, 3, 6]))
print(solution.is_straight2([1, 4, 5, 3, 6]))
print(solution.is_straight3([1, 4, 5, 3, 6]))
