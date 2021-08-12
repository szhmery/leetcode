from typing import List


class Solution:
    #复杂度分析：本方法优化时间复杂度的本质是通过判断舍去了不必要的递归（哨兵划分）。

    #时间复杂度 O(N) ： 其中 N 为数组元素数量；对于长度为 N 的数组执行哨兵划分操作的时间复杂度为 O(N) ；
    #每轮哨兵划分后根据 k 和 i 的大小关系选择递归，由于 i 分布的随机性，则向下递归子数组的平均长度为 N/2
    #因此平均情况下，哨兵划分操作一共有 N + N/2 + N/4 +...+N/N = (N-1/2)/(1-1/2)= 2N - 1（等比数列求和），即总体时间复杂度为 O(N) 。
    #空间复杂度 O(logN) ： 划分函数的平均递归深度为 O(logN) 。

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr):
            return arr

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i: #在左边继续寻找
                return quick_sort(l, i - 1)
            if k > i: #在右边继续寻找
                return quick_sort(i + 1, r)
            return arr[:k] #返回前k个值就是最小的k个值


        return quick_sort(0, len(arr) - 1)
