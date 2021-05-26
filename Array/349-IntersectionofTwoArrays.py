from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter_sec = set()
        for num in nums1:
            if num in nums2:
                inter_sec.add(num)
        return list(inter_sec)


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print("num1 {0} numn2 {1}".format(nums1, nums2))
    inter_set = solution.intersection(nums1, nums2)
    print("after intersection:{}".format(inter_set))

    nums1 = [4, 8, 1, 3]
    nums2 = [2, 2]
    print("num1 {0} numn2 {1}".format(nums1, nums2))
    inter_set = solution.intersection(nums1, nums2)
    print("after intersection:{}".format(inter_set))

    nums1 = [2, 1, 4, 5, 6]
    nums2 = [1, 0, 6]
    print("num1 {0} numn2 {1}".format(nums1, nums2))
    inter_set = solution.intersection(nums1, nums2)
    print("after intersection:{}".format(inter_set))