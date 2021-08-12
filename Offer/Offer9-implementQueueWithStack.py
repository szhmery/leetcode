class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack2 and not self.stack1:
            return -1
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()



# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(4)
obj.appendTail(5)
param_2 = obj.deleteHead()
print(param_2)



class CQueue2:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail2(self, value: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while self.stack2:
            self.stack1.append(self.stack2.pop())


    def deleteHead2(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1.pop()
