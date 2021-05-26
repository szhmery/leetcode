

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            raise Exception("The stack is empty!")
        value = self.stack.pop()
        if value <= self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        if len(self.minStack) == 0:
            raise Exception("The stack is empty!")
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    val = 1
    obj = MinStack()
    obj.push(val)
    obj.pop()
    obj.push(3)
    obj.push(2)
    obj.push(4)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print('top:{0}, min:{1}'.format(param_3, param_4))
