class MinStack:
    #时间复杂度 O(1) ： push(), pop(), top(), min() 四个函数的时间复杂度均为常数级别。
    #空间复杂度 O(N) ： 当共有 N 个待入栈元素时，辅助栈 B 最差情况下存储 N 个元素，使用 O(N) 额外空间。
    def __init__(self):

        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:#保证B的非严格降序，放入小于等于他栈顶的值。记得有=
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:#弹出的时候如果和最小栈栈顶值一样，把最小栈栈顶值也弹出。
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]

