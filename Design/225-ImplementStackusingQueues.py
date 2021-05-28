from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.put(x)
        s = self.queue.qsize()
        while s > 1:
            self.queue.put(self.queue.get())
            s -= 1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue.qsize() == 0

class MyStack2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()