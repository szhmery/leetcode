from typing import List


class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

    #https://leetcode.com/problems/find-the-duplicate-number/solution/
    # https://www.bilibili.com/video/BV1Ug4y1v7mF
    # slow and fast pointer,
    def findDuplicate2(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,3,4]
    print("Before move zeroes:{}".format(nums))
    result = solution.findDuplicate(nums)
    print("method 1:{}".format(result))

    result = solution.findDuplicate2(nums)
    print("method 1:{}".format(result))