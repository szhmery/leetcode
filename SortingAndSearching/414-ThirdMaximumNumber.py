from typing import List


class Solution:
    # https://leetcode.com/problems/third-maximum-number/discuss/90207/Intuitive-and-Short-Python-solution
    def thirdMax(self, nums: List[int]) -> int:
        v = [-float('inf'), -float('inf'), -float('inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:
                    v = [num, v[0], v[1]]
                elif num > v[1]:
                    v = [v[0], num, v[1]]
                elif num > v[2]:
                    v = [v[0], v[1], num]
        return max(v) if -float('inf') in v else v[2]

    # https://leetcode.com/problems/third-maximum-number/discuss/90202/Java-neat-and-easy-understand-solution-O(n)-time-O(1)-space
    def thirdMax2(self, nums: List[int]) -> int:
        max1 = -float('inf')
        max2 = -float('inf')
        max3 = -float('inf')
        for num in nums:
            if num == max1 or num == max2 or num == max3:
                continue
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        return max3 if max3 != -float('inf') else max1

    # by myself
    def thirdMax3(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if len(nums) < 3:
            return nums[0]
        k = 3
        pre = None
        for num in nums:
            if num != pre:
                pre = num
                k -= 1
            if k == 0:
                return num
        return nums[0]


solution = Solution()
mat = [1, 2, 3, 4]
result = solution.thirdMax(mat)
print(result)
mat = [1, 2, 2, 3]
result = solution.thirdMax(mat)
print(result)
mat = [1, 2]
result = solution.thirdMax(mat)
print(result)

mat = [1, 2, 3, 4]
result = solution.thirdMax2(mat)
print(result)
mat = [1, 2, 2, 3]
result = solution.thirdMax2(mat)
print(result)
mat = [1, 2]
result = solution.thirdMax2(mat)
print(result)
