from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter_sect = []
        for num in nums1:
            if num in nums2:
                inter_sect.append(num)
                nums2.remove(num)
        return inter_sect


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print("num1 {0} numn2 {1}".format(nums1, nums2))
    inter_set = solution.intersect(nums1, nums2)
    print("after intersection:{}".format(inter_set))

    nums1 = [4, 8, 1, 3]
    nums2 = [2, 2]
    print("num1 {0} numn2 {1}".format(nums1, nums2))
    inter_set = solution.intersect(nums1, nums2)
    print("after intersection:{}".format(inter_set))

    nums1 = [2, 1, 4, 5, 6]
    nums2 = [1, 0, 6]
    print("num1 {0} numn2 {1}".format(nums1, nums2))
    inter_set = solution.intersect(nums1, nums2)
    print("after intersection:{}".format(inter_set))
