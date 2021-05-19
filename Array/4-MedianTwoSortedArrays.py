from typing import List

class Solution:
    def findMedianSortedArrays(self, A, B):

        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, int((len1 + len2 + 1) / 2))
        else:
            return (self.getKth(nums1, nums2, int((len1 + len2) / 2)) + self.getKth(nums1, nums2, int(
                (len1 + len2) / 2 + 1))) * 0.5

    def getKth(self, nums1: List[int], nums2: List[int], k: int):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.getKth(nums2, nums1, k)
        if len1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        m = min(int(k / 2), len1)
        if nums1[m - 1] <= nums2[m - 1]:
            return self.getKth(nums1[m:], nums2, k - m)
        else:
            return self.getKth(nums1, nums2[m:], k - m)

    # https://www.bilibili.com/video/BV1gZ4y1K7gK?from=search&seid=1871222403625473150
    def findMedianSortedArrays2(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        if m == 0:
            return (B[(n-1)//2] + B[n//2])/2

        imin, imax = 0, m
        length = m + n
        while imin <= imax:
            cutA = int((imin + imax)/2) #选A中数据的个数
            cutB = int((length + 1)/2) - cutA #选B中数据的个数
            L1 = A[cutA-1] if cutA != 0 else -float('inf')
            L2 = B[cutB-1] if cutB != 0 else -float('inf')
            R1 = A[cutA] if cutA != m else float('inf')
            R2 = B[cutB] if cutB != n else float('inf')
            if L1 > R2:
                imax = cutA - 1
            elif L2 > R1:
                imin = cutA + 1
            else:
                if length % 2 == 0:
                    return (max(L1, L2) + min(R1, R2))/2
                else:
                    return max(L2,L2)
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(result)
    result = solution.findMedianSortedArrays2(nums1, nums2)
    print(result)