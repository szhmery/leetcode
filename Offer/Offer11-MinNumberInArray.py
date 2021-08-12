from typing import List


class Solution:
    #https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return
        if len(numbers) == 1:
            return numbers[0]
        l = 0
        r = len(numbers) - 1
        while l < r:
            mid = l + (r - l) // 2

            if numbers[mid] > numbers[r]: # mid is in the left
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1 # move r to left for 1 step.
        return numbers[l]



so = Solution()
print(so.minArray([]))
print(so.minArray([1]))
print(so.minArray([0,1]))
print(so.minArray([1,0]))
print(so.minArray([1,2,0]))
print(so.minArray([2,0,1]))
print(so.minArray([3,4,5,1,2]))
print(so.minArray([2,2,2,0,1]))
print(so.minArray([1,3,5]))
print(so.minArray([1,1,1,1,0,1,1]))