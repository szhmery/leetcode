from typing import List


class Solution:
    # 左边数的乘积乘以右边数的乘积
    def constructArr(self, a: List[int]) -> List[int]:
        ans = [1] * len(a)
        left_P = [1]* len(a)
        #先算左边数的乘积
        for i in range(1, len(a)):
            left_P[i] = left_P[i-1] * a[i-1]
        #后算右边数的乘积
        product_R = 1
        for j in range(len(a) - 1, -1, -1):
            ans[j] = product_R * left_P[j]
            product_R *= a[j]
        return ans

so = Solution()
print(so.constructArr([1,2,3,4,5]))

