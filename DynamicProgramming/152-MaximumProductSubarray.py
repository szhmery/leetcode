from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1JJ411V7PD?from=search&seid=16375649315385481561
    # DP
    def maxProduct(self, nums: List[int]) -> int:
        maxProductMemo = [None] * len(nums)
        minProductMemo = [None] * len(nums)

        maxProductMemo[0] = nums[0]
        minProductMemo[0] = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            maxProductMemo[i] = max(nums[i], maxProductMemo[i - 1] * nums[i], minProductMemo[i - 1] * nums[i])
            minProductMemo[i] = min(nums[i], maxProductMemo[i - 1] * nums[i], minProductMemo[i - 1] * nums[i])
            max_product = max(max_product, maxProductMemo[i])
        return max_product


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.maxProduct(nums)
    print('Max Product Sub Array:{}'.format(result))
