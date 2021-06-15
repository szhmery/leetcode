# Time:  O(n)
# Space: O(1)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if i % 2 == 0:  # odd
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:  # even
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5, 1, 1, 6, 4]
    solution.wiggleSort(nums)
    print(nums)
    nums = [1, 2, 3, 4]
    solution.wiggleSort(nums)
    print(nums)
