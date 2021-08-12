from typing import List

class Solution:
    #时间复杂度 O(N) ： 其中 N 为列表 pushed 的长度；每个元素最多入栈与出栈一次，即最多共 2N 次出入栈操作。
    #空间复杂度 O(N) ： 辅助栈 stack 最多同时存储 NN 个元素。

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0 #stack辅助栈
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 如果栈顶一样 循环判断与出栈
                stack.pop()
                i += 1 #把i +1，指向下一个popped的值
        return not stack

