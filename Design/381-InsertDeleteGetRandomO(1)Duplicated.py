import queue as Q
import random
import heapq

class RandomizedCollection:
    # https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/381.%20Insert%20Delete%20GetRandom%20O(1)%20-%20Duplicates%20allowed.md

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.hashtable = collections.defaultdict(set)
        self.array = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        valin = val not in self.hashtable
        self.hashtable[val].add(len(self.array))
        self.array.append(val)
        return valin

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hashtable:
            return False
        else:
            if self.array[-1] == val:
                removeIdx = len(self.array) - 1
                self.hashtable[val].remove(removeIdx)
            else:
                # set pop remove arbitrary element
                removeIdx = self.hashtable[val].pop()
                self.array[removeIdx] = self.array[-1]
                self.hashtable[self.array[-1]].remove(len(self.array) - 1)
                self.hashtable[self.array[-1]].add(removeIdx)
            if len(self.hashtable[val]) == 0:
                del self.hashtable[val]
            del self.array[-1]
            return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return random.choice(self.array)

# use PriorityQueue
# class RandomizedCollection2:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.datas = []
#         self.map_dict = {}
#
#
#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
#         """
#
#         if val not in self.map_dict:
#             que = []
#             heapq.heappush(que, len(self.datas))
#             self.map_dict[val] = que
#         else:
#             que = self.map_dict[val]
#             heapq.heappush(que, len(self.datas))
#             self.map_dict[val] = que
#         self.datas.append(val)
#         return len(self.map_dict[val]) == 1
#
#
#
#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the collection. Returns true if the collection contained the specified element.
#         """
#         if val not in self.map_dict:
#             return False
#         que_val = self.map_dict[val]
#         last = self.datas[-1]
#         last_idx = len(self.datas) - 1
#         if last == val:
#             heapq.heappushpop(que_val, last_idx)
#         else:
#             que_last = self.map_dict[last]
#             val_idx = heapq.heappop(que_val)
#             self.datas[val_idx] = self.datas[last_idx]
#             heapq.heappushpop(que_last, last_idx)
#             heapq.heappush(que_last, val_idx)
#         if len(self.map_dict[val]) == 0:
#             del self.map_dict[val]
#         del self.datas[-1]
#         return True
#
#
#     def getRandom(self) -> int:
#         """
#         Get a random element from the collection.
#         """
#         return random.choice(self.datas)

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection2()
param = obj.insert(1)
print(param)
param = obj.insert(1)
print(param)
param = obj.insert(2)
print(param)
param = obj.insert(1)
print(param)
param = obj.insert(2)
print(param)
param = obj.insert(2)
print(param)
param = obj.remove(1)
print(param)
param = obj.remove(2)
print(param)
param = obj.remove(2)
print(param)
param = obj.remove(2)
print(param)
param = obj.getRandom()
print(param)
param = obj.getRandom()
print(param)
param = obj.getRandom()
print(param)
param = obj.getRandom()
print(param)