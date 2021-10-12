class Solution:
    # 时间复杂度 O(10^n)： 递归的生成的排列的数量为 10^n - 1
    # 空间复杂度 O(10^n) ： 结果列表 res 的长度为 10^n - 1 ，各数字字符串的长度为 1, 2, ..., n因此占用 O(10^n) 大小的额外空间。
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n:  # 终止条件：已固定完所有位
                s = ''.join(num[self.start:])
                if s != '0':
                    res.append(int(s))  # 拼接 num 并添加至 res 尾部
                if n - self.start == self.nine:  # 当输出数字的所有位都是 9 时，则下个数字需要向更高位进 1
                    self.start -= 1
                return
            for i in range(10):  # 遍历 0 - 9
                if i == 9:
                    self.nine += 1
                num[x] = str(i)  # 固定第 x 位为 i
                dfs(x + 1)  # 开启固定第 x + 1 位
            self.nine -= 1

        num, res = ['0'] * n, []  # 起始数字定义为 n 个 0 组成的字符列表
        self.nine = 0
        self.start = n - 1  # start 规定字符串的左边界, 以保证添加的数字字符串 num[start:] 中无高位多余的 00
        dfs(0)  # 开启全排列递归
        return res


so = Solution()
print(so.printNumbers(3))
