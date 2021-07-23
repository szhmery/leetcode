from collections import defaultdict
from typing import List


class Solution:
    # https://leetcode.com/problems/next-greater-element-i/discuss/97595/Java-10-lines-linear-time-complexity-O(n)-with-explanation
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = defaultdict()
        ans = []
        # [9,8,7,3,2,1,6] 6 is the greater number of 3, 2, 1. Other greater numbers are -1
        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
        for num in nums1:
            ans.append(greater.get(num, -1))
        return ans

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_dict = {}
        ans = []
        for i in range(len(nums2)):
            nums2_dict[nums2[i]] = i
        for num in nums1:
            idx = nums2_dict[num]
            j = idx
            # for j in range(idx + 1, len(nums2)):  # the last j is not len(nums2), it's len(nums2) - 1. so choose while
            while j < len(nums2):
                if nums2[j] > num:
                    ans.append(nums2[j])
                    break
                j += 1
            if j == len(nums2):
                ans.append(-1)
        return ans


solution = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(solution.nextGreaterElement(nums1, nums2))
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(solution.nextGreaterElement(nums1, nums2))
