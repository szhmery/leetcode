from collections import OrderedDict


class LRUCache:
    # https://www.bilibili.com/video/BV1Wy4y147ds?from=search&seid=2110318775266469107
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.LRU:
            val = self.LRU[key]
            del self.LRU[key]
            self.LRU[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            del self.LRU[key]
            self.LRU[key] = value
        else:
            self.LRU[key] = value
            if len(self.LRU) > self.capacity:
                self.LRU.popitem(last=False)  # last =False FIFO


class LRUCache2:
    # https://www.bilibili.com/video/BV1qK411J7fe?from=search&seid=2110318775266469107
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.queue.remove(key)
            self.queue.insert(0, key)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.queue) == self.capacity:
            del self.cache[self.queue.pop(-1)]

        self.cache[key] = value
        self.queue.insert(0, key)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache2(2)

obj.put(1, 0)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
