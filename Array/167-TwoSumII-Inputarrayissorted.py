from typing import  List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        # mid = (lo + hi) // 2
        while lo < hi:
            if hi < len(numbers) and numbers[lo] + numbers[hi] == target:
                return [lo+1, hi+1]

            if numbers[lo] + numbers[hi] < target:
                lo += 1
            if numbers[lo] + numbers[hi] > target:
                hi -= 1
        return

if __name__ == "__main__":
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(numbers, target)
    print("nums {0}, method 1: target {1}, indices {2}".format(numbers, target, result))

