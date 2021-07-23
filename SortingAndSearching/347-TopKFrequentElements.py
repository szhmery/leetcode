import heapq
from collections import Counter
from typing import List
import random


class Solution:
    # https://www.bilibili.com/video/BV1sk4y1B7vj
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        q = []
        for num, freq in Counter(nums).items():
            if len(q) == k:
                heapq.heappushpop(q, (freq, num))
            else:
                heapq.heappush(q, (freq, num))
        return [x[1] for x in q]

    # https://leetcode.com/problems/top-k-frequent-elements/solution/
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)

    # Quickselect is a textbook algorithm typically used to solve the problems "find kth something": kth smallest,
    # kth largest, kth most frequent, kth less frequent, etc. Like quicksort, quickselect was developed by Tony Hoare,
    # and also known as Hoare's selection algorithm.
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
                # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]



if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print("Before:{}".format(nums))
    result = solution.topKFrequent(nums, k)
    print("method 1:{}".format(result))
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = solution.topKFrequent2(nums, k)
    print("method 2:{}".format(result))
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = solution.topKFrequent3(nums, k)
    print("method 3:{}".format(result))
    nums = [3, 0, 1, 0]
    k = 1
    print("Before:{}".format(nums))
    result = solution.topKFrequent(nums, k)
    print("method 1:{}".format(result))
