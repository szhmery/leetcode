from typing import List


class Solution:
    # 时间复杂度：O(n)，其中 n 是数组的长度。两个指针移动的总次数最多为 n 次。
    # 空间复杂度：O(1)。
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        # mid = (lo + hi) // 2
        while lo < hi:
            if hi < len(numbers) and numbers[lo] + numbers[hi] == target:
                return [lo + 1, hi + 1]
            if numbers[lo] + numbers[hi] < target:
                lo += 1
            if numbers[lo] + numbers[hi] > target:
                hi -= 1
        return [-1, -1]

    # binary search
    # 时间复杂度：O(nlogn)，其中 n 是数组的长度。需要遍历数组一次确定第一个数，时间复杂度是 O(n)，寻找第二个数使用二分查找，
    # 时间复杂度是 O(logn)，因此总时间复杂度是 O(nlogn)。
    # 空间复杂度：O(1)
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            lo, hi = i + 1, n - 1
            while lo <= hi: # binary search
                mid = lo + (hi - lo) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(numbers, target)
    print("nums {0}, method 1: target {1}, indices {2}".format(numbers, target, result))
    result = solution.twoSum2(numbers, target)
    print("nums {0}, method 1: target {1}, indices {2}".format(numbers, target, result))
