from typing import List
import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i, len(nums) - 1):
                for k in range(j, len(nums) - 2):
                    if nums[k] > nums[j] > nums[i]:
                        return True

        return False

    def increasingTriplet2(self, nums: List[int]) -> bool:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                if dp[i] >= 3:
                    return True
        return False

    def increasingTriplet3(self, nums: List[int]) -> bool:
        m1 = m2 = math.inf
        for num in nums:
            if m1 >= num:
                m1 = num
            elif m2 >= num:
                m2 = num
            else:
                return True
        return False

    def increasingTriplet4(self, nums: List[int]) -> bool:
        frontend = [nums[0]] * len(nums)
        backend = [nums[len(nums) - 1]] * len(nums)

        for i in range(len(nums)):
            frontend[i] = min(nums[i], frontend[i - 1])
        for j in range(len(nums)-2, 0, -1):
            backend[j] = max(nums[j], backend[j + 1])
        for k in range(len(nums)):
            if frontend[k] < nums[k] < backend[k]:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    print(nums)
    result = solution.increasingTriplet(nums)
    print('method1:{}'.format(result))
    result = solution.increasingTriplet2(nums)
    print('method2:{}'.format(result))
    result = solution.increasingTriplet3(nums)
    print('method3:{}'.format(result))
    result = solution.increasingTriplet4(nums)
    print('method4:{}'.format(result))

    nums = [2, 1, 5, 0, 4, 6]
    print(nums)
    result = solution.increasingTriplet(nums)
    print('method1:{}'.format(result))
    result = solution.increasingTriplet2(nums)
    print('method2:{}'.format(result))
    result = solution.increasingTriplet3(nums)
    print('method3:{}'.format(result))
    result = solution.increasingTriplet4(nums)
    print('method4:{}'.format(result))

    nums = [5,4,3,2,1]
    print(nums)
    result = solution.increasingTriplet(nums)
    print('method1:{}'.format(result))
    result = solution.increasingTriplet2(nums)
    print('method2:{}'.format(result))
    result = solution.increasingTriplet3(nums)
    print('method3:{}'.format(result))
    result = solution.increasingTriplet4(nums)
    print('method4:{}'.format(result))