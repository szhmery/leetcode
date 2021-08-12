class MaxQueue:

    def __init__(self):
        self.queue = []
        self.max_q = []


    def max_value(self) -> int:
        if not self.max_q:
            return -1
        return self.max_q[0]

    #维持max_q的单调队列，对头最大，依次递减
    def push_back(self, value: int) -> None:

        while self.max_q and self.max_q[-1] < value:#把比最大队列中小于当前值的值pop出来，维持单调递减队列
            self.max_q.pop()
        self.queue.append(value)
        self.max_q.append(value)

    #如果pop出的值和单调队列对头一样，单调队列也要pop出这个值
    def pop_front(self) -> int:
        if not self.queue:
            return -1
        value = self.queue.pop(0)
        if value == self.max_q[0]:
            self.max_q.pop(0)
        return value



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()