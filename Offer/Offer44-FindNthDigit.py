class Solution:
    # https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/mian-shi-ti-44-shu-zi-xu-lie-zhong-mou-yi-wei-de-6/
    # 时间复杂度 O(logn) ： 所求数位 n 对应数字 num 的位数 digit 最大为 O(logn) ；第一步最多循环O(logn) 次；
    # 第三步中将 num 转化为字符串使用 O(logn) 时间；因此总体为 O(logn) 。
    # 空间复杂度 O(logn) ： 将数字 num 转化为字符串 str(num) ，占用 O(logn) 的额外空间。

    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2.
        return int(str(num)[(n - 1) % digit]) # 3.

