from typing import List
import collections
import random


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.setdefault(num, 0) + 1
            if count_dict[num] > size // 2:
                return num
    # Brute Force
    # Time complexity : O(n^2)
    # Space complexity : O(1)
    def majorityElement(self, nums):
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num
    # HashMap
    # Time complexity : O(n)
    # Space complexity : O(n)
    def majorityElement2(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    #  Sorting
    # Time complexity O(nlgn)
    # Space complexity : O(1) or O(n)
    def majorityElement3(self, nums):
        nums.sort()
        return nums[len(nums)//2]

    # Randomization
    # Time complexity : O(∞)
    # Space complexity : O(1)
    def majorityElement4(self, nums):
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate

    # Divide and Conquer
    # Time complexity : O(nlgn)
    # Space complexity : O(nlgn)
    def majorityElement5(self, nums):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)
    # quick sort
    #O(nlogn)
    import random
    def majorityElement_quicksort(self, nums):
        def partition(nums, low, high):
            if low == high:
                return low
            p = low + random.randrange(high - low + 1)
            # pivot = nums[random.randint(left, right)]
            pivot = nums[p]
            nums[p], nums[high] = nums[high], nums[p]

            small = low - 1
            for i in range(low, high):
                if nums[i] < pivot:
                    small += 1
                    if i != small:
                        nums[small], nums[i] = nums[i], nums[small]

            small += 1
            nums[small], nums[high] = nums[high], nums[small]
            return small

        n = len(nums)
        mid = n // 2
        start = 0
        end = n - 1
        index = partition(nums, start, end)
        while index != mid:
            if index > mid:
                end = index - 1
                index = partition(nums, start, end)
            else:
                start = index + 1
                index = partition(nums, start, end)
        ans = nums[mid]
        return ans



    # Boyer-Moore Voting Algorithm
    # Time complexity : O(n)
    # Space complexity : O(1)
    def majorityElement6(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


if __name__ == '__main__':
    solution = Solution()
    tokens = [1, 2, 2, 5, 6, 2, 2]
    result = solution.majorityElement(tokens)
    print(result)
    result = solution.majorityElement2(tokens)
    print(result)
    result = solution.majorityElement3(tokens)
    print(result)
    result = solution.majorityElement4(tokens)
    print(result)
    result = solution.majorityElement5(tokens)
    print(result)
    tokens = [4,5,4]
    result = solution.majorityElement_quicksort(tokens)
    print(result)


