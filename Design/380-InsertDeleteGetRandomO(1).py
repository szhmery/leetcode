import random

class RandomizedSet:

    # https://www.cnblogs.com/grandyang/p/5740864.html
    # https://www.bilibili.com/video/BV1Fg4y1q7Ru
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.datas = []
        self.map_dict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map_dict:
            return False
        self.datas.append(val)
        self.map_dict[val] = len(self.datas) - 1
        return True
    # 由于 HashMap 的删除是常数时间的，而数组并不是，为了使数组删除也能常数级，实际上将要删除的数字和数组的最后一个数字调换个位置，
    # 然后修改对应的 HashMap 中的值，这样只需要删除数组的最后一个元素即可，保证了常数时间内的删除
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map_dict:
            return False
        last = self.datas[-1]
        idx = self.map_dict[val]
        self.map_dict[last] = idx
        self.datas[idx] = last

        del self.datas[-1]
        del self.map_dict[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # n = len(self.datas)
        # if n == 0:
        #    return False
        # index = random.randint(1, len(self.datas))
        # return self.datas[index - 1]
        return random.choice(self.datas)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()