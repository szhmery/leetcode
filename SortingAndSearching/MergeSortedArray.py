from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[m:] = nums2.copy()
            return
        if n == 0:
            return
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(nums1)
    print(nums2)
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)
