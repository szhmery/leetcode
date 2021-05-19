from typing import List


class Solution:
    # https://leetcode.com/problems/remove-element/solution/
    # Two Pointers
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    #Two Pointers - when elements to remove are rare
    def removeElement2(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n

    def removeElement3(self, nums: List[int], val: int) -> int:
        count = 0
        if nums is None:
            return 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    print("Before:")
    print(nums)
    print("After:")
    print(solution.removeElement(nums, 2))
    print(nums)