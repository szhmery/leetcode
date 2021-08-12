from typing import List


class Solution:
    # 时间复杂度 O(NlogN) ： 其中 NN 为数组长度；归并排序使用 O(NlogN) 时间；
    # 空间复杂度 O(N) ： 辅助数组 tmptmp 占用 O(N) 大小的额外空间；

    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            # 终止条件
            if l >= r:
                return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]  # tmp 暂存nums从l到r+1的数字
            for k in range(l, r + 1):
                if i == m + 1:  # 左边结束，把右边一个个考过来
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:  # 如果左边比右边大，计算逆序数对数
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1  # 统计逆序对
            return res

        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)

    def reversePairs2(self, nums: List[int]) -> int:
        def mergeSort(nums, tmp, l, r):
            if l >= r:
                return 0

            mid = (l + r) // 2
            inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
            i, j, pos = l, mid + 1, l
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    tmp[pos] = nums[i]
                    i += 1
                    inv_count += (j - (mid + 1))
                else:
                    tmp[pos] = nums[j]
                    j += 1
                pos += 1
            for k in range(i, mid + 1):
                tmp[pos] = nums[k]
                inv_count += (j - (mid + 1))
                pos += 1
            for k in range(j, r + 1):
                tmp[pos] = nums[k]
                pos += 1
            nums[l:r + 1] = tmp[l:r + 1]
            return inv_count


        n = len(nums)
        tmp = [0] * n
        return mergeSort(nums, tmp, 0, n - 1)
