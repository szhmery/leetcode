from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1oT4y1G78Y?from=search&seid=15213169886991285961
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        # left -> right
        for i in range(1, n ):
            ans[i] = ans[i - 1] * nums[i - 1]
        product_R = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= product_R
            product_R *= nums[i]
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    result = solution.productExceptSelf(nums)
    print('produce except self:{}'.format(result))
    nums = [-1, 1, 0, -3, 3]
    result = solution.productExceptSelf(nums)
    print('produce except self:{}'.format(result))